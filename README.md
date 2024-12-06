## Cloud Service Access Management System
### with MongoDB, Postman, and PyCharm: Dynamic access control, subscription management, and usage tracking for cloud APIs.

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

1. Start MongoDB:
    - Ensure that your MongoDB server is running.

2. Open PyCharm:
    - Open PyCharm IDE on your computer.

3. Open Project:
    - Open the Cloud Service Access Management System project in PyCharm.

4. Run the FastAPI Application:
    - Run the FastAPI application by executing the main.py script.
    - Verify that the application is running without errors.

5. Insert Default Sample Data:
    - Check if the default sample data is inserted successfully by looking for the "Default sample data inserted successfully" message in the console.

6. Open Postman:
    - Open the Postman application on your computer.

7. **Create Plan:**
    - Use Postman to create a new plan by sending a POST request to `http://127.0.0.1:8001/plans` with a JSON body containing plan details.
    - **Example JSON Body:**
    ```json
    { "plan_name": "Silver Plan", "description": "Moderate access", "api_permissions": ["api1", "api3"], "usage_limits": {"api1": 200, "api3": 100} }
    ```
    - **Expected Response:**
    ```json
    {
        "message": "Plan created successfully",
        "plan_id": "Generated Plan ID"
    }
    ```

8. **Get All Plans:**
    - Retrieve all plans using Postman by sending a GET request to `http://127.0.0.1:8001/plans`.
    - Verify that the newly created plan is listed.

9. **Modify Plan:**
    - Modify the plan using Postman by sending a PUT request to `http://127.0.0.1:8001/plans/{plan_id}` with the updated plan details.
    - **Example URL:**
    ```
    http://127.0.0.1:8001/plans/{plan_id}
    ```
    - **Example JSON Body:**
    ```json
    {
        "plan_name": "Silver Plan",
        "description": "Moderate access",
        "api_permissions": ["api1", "api3", "api5"],
        "usage_limits": {"api1": 200, "api3": 100, "api5": 50}
    }
    ```
    - **Expected Response:**
    ```json
    {
        "message": "Plan modified successfully"
    }
    ```

10. **Delete Plan:**
    - Delete the plan using Postman by sending a DELETE request to `http://127.0.0.1:8001/plans/{plan_id}`.
    - **Example URL:**
    ```
    http://127.0.0.1:8001/plans/{plan_id}
    ```
    - **Expected Response:**
    ```json
    {
        "message": "Plan deleted successfully"
    }
    ```

11. **Subscribe to Plan:**
    - Subscribe a user to a plan using Postman by sending a POST request to `http://127.0.0.1:8001/subscriptions` with a JSON body containing subscription details.
    - **Example JSON Body:**
    ```json
    { "user_id": "user456", "plan_id": "{plan_id}", "subscribed_at": "2023-01-01T12:00:00", "api_permissions": ["api1", "api3"] }
    ```
    - **Expected Response:**
    ```json
    {
        "message": "Subscribed successfully",
        "subscription_id": "Generated Subscription ID"
    }
    ```

12. **Check Access Permission:**
    - Check access permission using Postman by sending a GET request to `http://127.0.0.1:8001/access/{user_id}/{api_request}`.
    - **Example URL:**
    ```
    http://127.0.0.1:8001/access/user456/api1
    ```
    - **Expected Response:**
    ```json
    {
        "message": "Access granted"
    }
    ```

13. **Track API Request:**
    - Track an API request using Postman by sending a POST request to `http://127.0.0.1:8001/usage/user456` with a JSON body containing usage details.
    - **Example JSON Body:**
    ```json
    { "user_id": "user456", "api_request": "/api1", "timestamp": "2023-01-01T12:15:00" }
    ```
    - **Expected Response:**
    ```json
    {
        "message": "API request tracked successfully"
    }
    ```

14. **Check Limit Status:**
    - Check the limit status using Postman by sending a GET request to `http://127.0.0.1:8001/usage/user456/limit`.
    - **Expected Response:**
    ```json
    {
        "message": "Within limit"
    }
    ```

This script outlines the steps to demonstrate the key features of the Cloud Service Access Management System using PyCharm, MongoDB, and Postman.
