import uvicorn
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Connect to MongoDB
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client["cloud_service_management"]

# Collections
plans_collection = db["plans"]
permissions_collection = db["permissions"]
subscriptions_collection = db["subscriptions"]
usage_collection = db["usage"]

# MongoDB connection check
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

class Plan(BaseModel):
    plan_id: Optional[str] = None
    plan_name: str
    description: str
    api_permissions: List[str]
    usage_limits: dict

class Permission(BaseModel):
    permission_id: Optional[str] = None
    permission_name: str
    api_endpoint: str
    description: str

class Subscription(BaseModel):
    user_id: str
    plan_id: str  # Include plan_id in Subscription model
    subscribed_at: datetime
    api_permissions: List[str]  # Include api_permissions in Subscription model

class Usage(BaseModel):
    user_id: str
    api_request: str
    timestamp: datetime

# Insert default sample data
def insert_default_sample_data():
    try:
        # Insert sample plan data
        sample_plan_data = {
            "plan_name": "Basic Plan",
            "description": "Limited access",
            "api_permissions": ["api1", "api2"],
            "usage_limits": {"api1": 100, "api2": 50}
        }

        plan_id = plans_collection.insert_one(sample_plan_data).inserted_id

        # Insert sample permission data
        sample_permission = {
            "permission_name": "api3",
            "api_endpoint": "/api3",
            "description": "Sample API 3"
        }
        permissions_collection.insert_one(sample_permission)

        # Insert sample subscription data
        sample_subscription = Subscription(
            user_id="user123",
            plan_id=str(plan_id),  # Use the generated plan_id
            subscribed_at=datetime.now(),
            api_permissions=["api1", "api2"]  # Define appropriate permissions
        )
        subscriptions_collection.insert_one(sample_subscription.dict())

        # Insert sample usage data
        sample_usage = Usage(
            user_id="user123",
            api_request="/api1",
            timestamp=datetime.now()
        )
        usage_collection.insert_one(sample_usage.dict())

        print("Default sample data inserted successfully")

    except Exception as e:
        print(f"Error inserting default sample data: {e}")


# Create Plan
@app.post("/plans")
async def create_plan(plan_data: Plan):
    plan_id = plans_collection.insert_one(plan_data.dict()).inserted_id
    return {"message": "Plan created successfully", "plan_id": str(plan_id)}

# Get All Plans
@app.get("/plans")
async def get_all_plans():
    plans = plans_collection.find()
    return [Plan(**plan) for plan in plans]

# Modify Plan
@app.put("/plans/{plan_id}")
async def modify_plan(plan_id: str, plan_data: Plan):
    result = plans_collection.update_one({"_id": ObjectId(plan_id)}, {"$set": plan_data.dict()})
    if result.modified_count == 1:
        return {"message": "Plan modified successfully"}
    else:
        raise HTTPException(404, "Plan not found")

# Delete Plan
@app.delete("/plans/{plan_id}")
async def delete_plan(plan_id: str):
    result = plans_collection.delete_one({"_id": ObjectId(plan_id)})
    if result.deleted_count == 1:
        return {"message": "Plan deleted successfully"}
    else:
        raise HTTPException(404, "Plan not found")

# Add Permission
@app.post("/permissions")
async def add_permission(permission_data: Permission):
    permission_id = permissions_collection.insert_one(permission_data.dict()).inserted_id
    return {"message": "Permission added successfully", "permission_id": str(permission_id)}

# Get All Permissions
@app.get("/permissions")
async def get_all_permissions():
    permissions = permissions_collection.find()
    return [Permission(**permission) for permission in permissions]

# Modify Permission
@app.put("/permissions/{permission_id}")
async def modify_permission(permission_id: str, permission_data: Permission):
    result = permissions_collection.update_one({"_id": ObjectId(permission_id)}, {"$set": permission_data.dict()})
    if result.modified_count == 1:
        return {"message": "Permission modified successfully"}
    else:
        raise HTTPException(404, "Permission not found")

# Delete Permission
@app.delete("/permissions/{permission_id}")
async def delete_permission(permission_id: str):
    result = permissions_collection.delete_one({"_id": ObjectId(permission_id)})
    if result.deleted_count == 1:
        return {"message": "Permission deleted successfully"}
    else:
        raise HTTPException(404, "Permission not found")

# Subscribe to Plan
@app.post("/subscriptions")
async def subscribe_to_plan(subscription_data: Subscription):
    subscription_id = subscriptions_collection.insert_one(subscription_data.dict()).inserted_id
    return {"message": "Subscribed successfully", "subscription_id": str(subscription_id)}

# Get Subscription Details
@app.get("/subscriptions/{user_id}")
async def get_subscription_details(user_id: str):
    subscription = subscriptions_collection.find_one({"user_id": user_id})
    if subscription:
        return Subscription(**subscription)
    else:
        raise HTTPException(404, "Subscription not found")

# Assign/Modify User Plan
@app.put("/subscriptions/{user_id}")
async def assign_modify_user_plan(user_id: str, subscription_data: Subscription):
    result = subscriptions_collection.update_one({"user_id": user_id}, {"$set": subscription_data.dict()})
    if result.modified_count == 1:
        return {"message": "User plan assigned/modified successfully"}
    else:
        raise HTTPException(404, "User not found or plan not modified")

# Check Access Permission
@app.get("/access/{user_id}/{api_request}")
async def check_access_permission(user_id: str, api_request: str):
    subscription = subscriptions_collection.find_one({"user_id": user_id})
    if subscription and api_request in subscription.get("api_permissions", []):
        return {"message": "Access granted"}
    else:
        print(f"Access denied for {user_id} - {api_request}")
        raise HTTPException(403, "Access denied")

# Track API Request
@app.post("/usage/{user_id}")
async def track_api_request(user_id: str, usage_data: Usage):
    usage_collection.insert_one(usage_data.dict())
    return {"message": "API request tracked successfully"}

# Check Limit Status
@app.get("/usage/{user_id}/limit")
async def check_limit_status(user_id: str):
    usage_count = usage_collection.count_documents({"user_id": user_id})
    subscription = subscriptions_collection.find_one({"user_id": user_id})
    if usage_count > subscription.get("usage_limits", 0):
        # if usage_count <= subscription.get("usage_limits", 0):
        return {"message": "Within limit"}
    else:
        raise HTTPException(403, "Exceeded usage limit")

# Insert default sample data
if __name__ == "__main__":
    insert_default_sample_data()
    uvicorn.run("main:app", host="127.0.0.1", port=8001)
