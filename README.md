## Cloud Service Access Management System
### with MongoDB, Postman, and VS Code: Dynamic access control, subscription management, and usage tracking for cloud APIs.

Team Members :  Shwetank Singh (CWID:813968286) & Mahitha Pasupuleti (CWID:867114134)

[Stream Project Working Video](https://drive.google.com/file/d/1PxyPnPNhcn75oFr7ePQ9ROM-n2eueks1/view?usp=sharing) 

## Steps to run the application:
1. Create environment and activate.
2. Run command `pip install -r requirements.txt` to install all dependencies.
3. Run command `py main.py` to run the application.
4. Test through Postman on [http://localhost:8001/*](http://localhost:8001/*).

## API Details:

The code defines the following APIs:

1. **Create Plan API**
    - Method: POST
    - Path: "/plans"
    - Description: Create a new subscription plan.

2. **Get All Plans API**
    - Method: GET
    - Path: "/plans"
    - Description: Retrieve details of all subscription plans.

3. **Modify Plan API**
    - Method: PUT
    - Path: "/plans/{plan_id}"
    - Description: Modify details of a specific subscription plan.

4. **Delete Plan API**
    - Method: DELETE
    - Path: "/plans/{plan_id}"
    - Description: Delete a specific subscription plan.

5. **Add Permission API**
    - Method: POST
    - Path: "/permissions"
    - Description: Add a new permission.

6. **Get All Permissions API**
    - Method: GET
    - Path: "/permissions"
    - Description: Retrieve details of all permissions.

7. **Modify Permission API**
    - Method: PUT
    - Path: "/permissions/{permission_id}"
    - Description: Modify details of a specific permission.

8. **Delete Permission API**
    - Method: DELETE
    - Path: "/permissions/{permission_id}"
    - Description: Delete a specific permission.

9. **Subscribe to Plan API**
    - Method: POST
    - Path: "/subscriptions"
    - Description: Subscribe to a specific plan.

10. **Get Subscription Details API**
    - Method: GET
    - Path: "/subscriptions/{user_id}"
    - Description: Retrieve subscription details for a specific user.

11. **Assign/Modify User Plan API**
    - Method: PUT
    - Path: "/subscriptions/{user_id}"
    - Description: Assign or modify the subscription plan for a specific user.

12. **Check Access Permission API**
    - Method: GET
    - Path: "/access/{user_id}/{api_request}"
    - Description: Check if a user has access permission for a specific API request.

13. **Track API Request API**
    - Method: POST
    - Path: "/usage/{user_id}"
    - Description: Track an API request made by a user.

14. **Check Limit Status API**
    - Method: GET
    - Path: "/usage/{user_id}/limit"
    - Description: Check the usage limit status for a specific user.

## Testing API:

### Initial Setup:
1. **Start MongoDB:**
    - Ensure that your MongoDB server is running.

2. **Open VS Code:**
    - Open the VS Code IDE on your computer.

3. **Open Project:**
    - Open the Cloud Service Access Management System project in PyCharm.

4. **Run the FastAPI Application:**
    - Run the FastAPI application by executing the `main.py` script.
    - Verify that the application is running without errors.

5. **Insert Default Sample Data:**
    - Check if the default sample data is inserted successfully by looking for the "Default sample data inserted successfully" message in the console.

### Testing with Postman:

#### Plan Management:
1. **Create Plan:**
    - **Endpoint:** `POST /plans`
    - **Example JSON Body:**
    ```json
    { 
      "plan_name": "Silver Plan", 
      "description": "Moderate access", 
      "api_permissions": ["api1", "api3"], 
      "usage_limits": {"api1": 200, "api3": 100} 
    }
    ```
    - **Expected Response:**
    ```json
    {
        "message": "Plan created successfully",
        "plan_id": "Generated Plan ID"
    }
    ```

2. **Create Pro Plan:**
    - **Endpoint:** `POST /plans`
    - **Example JSON Body:**
    ```json
    {
      "plan_name": "Pro Plan",
      "description": "Access to all APIs with extended limits",
      "api_permissions": ["api1", "api2", "api3"],
      "usage_limits": {
        "api1": 500,
        "api2": 300,
        "api3": 100
      }
    }
    ```

3. **Get All Plans:**
    - **Endpoint:** `GET /plans`
    - No body required.

4. **Modify Plan:**
    - **Endpoint:** `PUT /plans/{plan_id}`
    - **Example JSON Body:**
    ```json
    {
      "plan_name": "Pro Plan Updated",
      "description": "Updated description for Pro Plan",
      "api_permissions": ["api1", "api2", "api3", "api4"],
      "usage_limits": {
        "api1": 600,
        "api2": 400,
        "api3": 150,
        "api4": 50
      }
    }
    ```

5. **Delete Plan:**
    - **Endpoint:** `DELETE /plans/{plan_id}`
    - No body required. Replace `{plan_id}` with the appropriate ID.

#### Permission Management:
1. **Add Permission:**
    - **Endpoint:** `POST /permissions`
    - **Example JSON Body:**
    ```json
    {
      "permission_name": "api4",
      "api_endpoint": "/api4",
      "description": "Access to advanced analytics"
    }
    ```

2. **Modify Permission:**
    - **Endpoint:** `PUT /permissions/{permission_id}`
    - **Example JSON Body:**
    ```json
    {
      "permission_name": "api4-updated",
      "api_endpoint": "/api4-updated",
      "description": "Updated description for api4"
    }
    ```

3. **Delete Permission:**
    - **Endpoint:** `DELETE /permissions/{permission_id}`
    - No body required. Replace `{permission_id}` with the appropriate ID.

4. **Get All Permissions:**
    - **Endpoint:** `GET /permissions`
    - No body required.

#### Subscription Management:
1. **Subscribe to Plan:**
    - **Endpoint:** `POST /subscriptions`
    - **Example JSON Body:**
    ```json
    {
      "user_id": "user456",
      "plan_id": "your_plan_id_here", 
      "subscribed_at": "2024-12-06T10:00:00",
      "api_permissions": ["api1", "api3"]
    }
    ```

2. **Assign/Modify User Plan:**
    - **Endpoint:** `PUT /subscriptions/{user_id}`
    - **Example JSON Body:**
    ```json
    {
      "user_id": "user456",
      "plan_id": "your_updated_plan_id_here", 
      "subscribed_at": "2024-12-06T12:00:00",
      "api_permissions": ["api1", "api2", "api4"]
    }
    ```

3. **Get Subscription Details:**
    - **Endpoint:** `GET /subscriptions/{user_id}`
    - No body required. Replace `{user_id}` with `user456`.

4. **Delete Subscription:**
    - **Endpoint:** `DELETE /subscriptions/{user_id}`
    - No body required. Replace `{user_id}` with `user456`.

#### API Usage and Access:
1. **Check Access Permission:**
    - **Endpoint:** `GET /access/{user_id}/{api_request}`
    - Replace `{user_id}` with `user456` and `{api_request}` with `/api3`.

2. **Track API Request:**
    - **Endpoint:** `POST /usage/{user_id}`
    - **Example JSON Body:**
    ```json
    {
      "user_id": "user456",
      "api_request": "/api3",
      "timestamp": "2024-12-06T11:00:00"
    }
    ```

3. **Check Limit Status:**
    - **Endpoint:** `GET /usage/{user_id}/limit`
    - No body required. Replace `{user_id}` with `user456`.

4. **Reset API Usage:**
    - **Endpoint:** `PUT /usage/reset/{user_id}`
    - No body required. Replace `{user_id}` with `user456`.

#### Admin Functionality:
1. **Get System Statistics:**
    - **Endpoint:** `GET /admin/statistics`
    - No body required.

2. **Reset All API Usage:**
    - **Endpoint:** `PUT /admin/usage/reset`
    - No body required.

This document outlines the steps to demonstrate the key features of the Cloud Service Access Management System using VS Code, MongoDB, and Postman.

