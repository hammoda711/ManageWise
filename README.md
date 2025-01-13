# API Documentation

## Overview

This documentation provides an overview of the endpoints available in the API, including registration, authentication, and employee,company and department management. It also outlines the permissions used for access control.

---

## Authentication and Authorization

### Permissions

The following permissions are implemented to control access to the API:

1. **IsAdminOrManager**:
  - Admin users have full access to all endpoints.
  - Managers have access to view and modify employees but cannot delete them.
2. **IsAdminManagerOrEmployee**:
  - Admin users have full access to all endpoints.
  - Managers have access to view and modify employees but cannot delete them.
  - Employees can view their own data but cannot modify or delete it.
  - Unauthenticated users have no access.

### Required Headers

All requests requiring authentication must include the following header:

```http
Authorization: Bearer <your_jwt_access_token>
Content-Type: application/json
```

---

## Endpoints

### 1. User Registration

**Endpoint:** `/api/accounts/register/`

- **Method:** `POST`
  
- **Description:** Allows new users to register.
  
- **Request Body:**
  
  ```json
  {
      "email": "user@example.com",
      "username": "username",
      "password": "securepassword",
      "role": "employee"  // Options: "admin", "manager", "employee"
  }
  ```
  
- **Response:**
  
  ```json
  {
      "id": 1,
      "email": "user@example.com",
      "username": "username",
      "role": "employee"
  }
  ```
  

---

### 2. User Login

**Endpoint:** `/api/accounts/login/`

- **Method:** `POST`
  
- **Description:** Authenticates a user and provides a JWT token.
  
- **Request Body:**
  
  ```json
  {
      "email": "user@example.com",
      "password": "securepassword"
  }
  ```
  
- **Response:**
  
  ```json
  {
      "access": "<jwt_access_token>",
      "refresh": "<jwt_refresh_token>"
  }
  ```
  

---

### 3. Token Refresh

**Endpoint:** `/api/accounts/token/refresh/`

- **Method:** `POST`
  
- **Description:** Refreshes an expired JWT access token.
  
- **Request Body:**
  
  ```json
  {
      "refresh": "<jwt_refresh_token>"
  }
  ```
  
- **Response:**
  
  ```json
  {
      "access": "<new_jwt_access_token>"
  }
  ```
  

---

### 4. Employee ViewSet

**Base Endpoint:** `/api/employees/`

#### a. List Employees

- **Endpoint:** `/api/employees/`
  
- **Method:** `GET`
  
- **Description:** Retrieves a list of all employees.
  
- **Access:** Admins and Managers only.
  
- **Response:**
  
  ```json
  [
      {
          "id": 1,
          "user": 1,
          "company": "Company Name",
          "department": "Department Name",
          "name": "John Doe",
          "email": "john.doe@example.com",
          "mobile_number": "+1234567890",
          "address": "123 Main Street",
          "designation": "Software Engineer",
          "hired_on": "2023-05-15",
          "days_employed": 200
      }
  ]
  ```
  

#### b. Retrieve Employee Details

- **Endpoint:** `/api/employees/{id}/`
- **Method:** `GET`
- **Description:** Retrieves details of a specific employee.
- **Access:** Admins, Managers, or the employee themselves.

#### c. Create Employee

- **Endpoint:** `/api/employees/`
  
- **Method:** `POST`
  
- **Description:** Creates a new employee record.
  
- **Access:** Admins and Managers only.
  
- **Request Body:**
  
  ```json
  {
      "user": 1,
      "company": 2,
      "department": 3,
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "mobile_number": "+9876543210",
      "address": "456 Another Street",
      "designation": "Project Manager",
      "hired_on": "2023-06-01"
  }
  ```
  

#### d. Update Employee Details

- **Endpoint:** `/api/employees/{id}/`
  
- **Method:** `PUT` or `PATCH`
  
- **Description:** Updates an employee record.
  
- **Access:** Admins and Managers only.
  
- **Request Body (Example for PATCH):**
  
  ```json
  {
      "designation": "Senior Software Engineer",
      "address": "789 Updated Street"
  }
  ```
  

#### e. Delete Employee

- **Endpoint:** `/api/employees/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes an employee record.
- **Access:** Admins only.

---

## Notes

1. Replace `{id}` in the endpoints with the actual ID of the employee.
2. Ensure the JWT token is included in the headers for authenticated requests.
3. Permissions are enforced to prevent unauthorized access to resources.

---

## Company Management Endpoints

### 1. List Companies

- **Endpoint:** `/api/companies/`
- **Method:** `GET`
- **Description:** Retrieves a list of all companies.
- **Access:** Admins and Managers only.

#### Response:

```json
[
  {
    "id": 1,
    "name": "TechCorp",
    "location": "New York",
    "industry": "Technology"
  }
]
```

### 2. Retrieve Company Details

- **Endpoint:** `/api/companies/{id}/`
- **Method:** `GET`
- **Description:** Retrieves details of a specific company.
- **Access:** Admins and Managers only.

#### Response:

```json
{
  "id": 1,
  "name": "TechCorp",
  "location": "New York",
  "industry": "Technology"
}
```

### 3. Create Company

- **Endpoint:** `/api/companies/`
- **Method:** `POST`
- **Description:** Creates a new company record.
- **Access:** Admins and Managers only.

#### Request Body:

```json
{
  "name": "Innovative Solutions",
  "location": "San Francisco",
  "industry": "Consulting"
}
```

#### Response:

```json
{
  "id": 2,
  "name": "Innovative Solutions",
  "location": "San Francisco",
  "industry": "Consulting"
}
```

### 4. Update Company Details

- **Endpoint:** `/api/companies/{id}/`
- **Method:** `PUT` or `PATCH`
- **Description:** Updates a company record.
- **Access:** Admins and Managers only.

#### Request Body:

```json
{
  "name": "Innovative Solutions Inc.",
  "location": "San Francisco",
  "industry": "Consulting"
}
```

#### Response:

```json
{
  "id": 2,
  "name": "Innovative Solutions Inc.",
  "location": "San Francisco",
  "industry": "Consulting"
}
```

### 5. Delete Company

- **Endpoint:** `/api/companies/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes a company record.
- **Access:** Admins only.

---

## Department Management Endpoints

### 1. List Departments

- **Endpoint:** `/api/departments/`
- **Method:** `GET`
- **Description:** Retrieves a list of all departments.
- **Access:** Admins and Managers only.

#### Response:

```json
[
  {
    "id": 1,
    "name": "Software Development",
    "company": 1,
    "location": "New York"
  }
]
```

### 2. Retrieve Department Details

- **Endpoint:** `/api/departments/{id}/`
- **Method:** `GET`
- **Description:** Retrieves details of a specific department.
- **Access:** Admins and Managers only.

#### Response:

```json
{
  "id": 1,
  "name": "Software Development",
  "company": 1,
  "location": "New York"
}
```

### 3. Create Department

- **Endpoint:** `/api/departments/`
- **Method:** `POST`
- **Description:** Creates a new department record.
- **Access:** Admins and Managers only.

#### Request Body:

```json
{
  "name": "Marketing",
  "company": 2,
  "location": "San Francisco"
}
```

#### Response:

```json
{
  "id": 2,
  "name": "Marketing",
  "company": 2,
  "location": "San Francisco"
}
```

### 4. Update Department Details

- **Endpoint:** `/api/departments/{id}/`
- **Method:** `PUT` or `PATCH`
- **Description:** Updates a department record.
- **Access:** Admins and Managers only.

#### Request Body:

```json
{
  "name": "Digital Marketing",
  "company": 2,
  "location": "San Francisco"
}
```

#### Response:

```json
{
  "id": 2,
  "name": "Digital Marketing",
  "company": 2,
  "location": "San Francisco"
}
```

### 5. Delete Department

- **Endpoint:** `/api/departments/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes a department record.
- **Access:** Admins only.

---

## Employee Performance Review Cycle Workflow Endpoints

### 1. Create Performance Review

- **Endpoint:** `/api/reviews/`
- **Method:** `POST`
- **Description:** Initiates a new performance review for an employee.
- **Access:** Admins and Managers only.

#### Request Body:

```json
{
  "employee_id": 1,
  "review_date": "2025-02-01",
  "stage": "Pending Review"
}
```

#### Response:

```json
{
  "id": 1,
  "employee_id": 1,
  "review_date": "2025-02-01",
  "stage": "Pending Review"
}
```

### 2. Schedule Review

- **Endpoint:** `/api/reviews/{id}/schedule/`
- **Method:** `POST`
- **Description:** Updates the stage to "Review Scheduled" after confirming the review date.
- **Access:** Admins and Managers only.

#### Response:

```json
{
  "id": 1,
  "stage": "Review Scheduled",
  "review_date": "2025-02-01"
}
```

### 3. Provide Feedback

- **Endpoint:** `/api/reviews/{id}/feedback/`
- **Method:** `POST`
- **Description:** Allows the manager to provide feedback after the review meeting.
- **Access:** Admins and Managers only.

#### Request Body:

```json
{
  "feedback": "The employee has shown improvement in their project management skills."
}
```

#### Response:

```json
{
  "id": 1,
  "feedback": "The employee has shown improvement in their project management skills.",
  "stage": "Feedback Provided"
}
```

### 4. Submit for Managerial Approval

- **Endpoint:** `/api/reviews/{id}/approve/`
- **Method:** `POST`
- **Description:** Submits the feedback for approval, updating the stage to "Under Approval."
- **Access:** Admins and Managers only.

#### Response:

```json
{
  "id": 1,
  "stage": "Under Approval"
}
```

### 5. Approve Review

- **Endpoint:** `/api/reviews/{id}/approve/`
- **Method:** `POST`
- **Description:** Manager approves the feedback and finalizes the review.
- **Access:** Admins and Managers only.

#### Response:

```json
{
  "id": 1,
  "stage": "Review Approved"
}
```

### 6. Reject Review

- **Endpoint:** `/api/reviews/{id}/reject/`
- **Method:** `POST`
- **Description:** If feedback is rejected, the stage is set to "Review Rejected."
- **Access:** Admins and Managers only.

#### Response:

```json
{
  "id": 1,
  "stage": "Review Rejected"
}
```

### 7. Update Rejected Review

- **Endpoint:** `/api/reviews/{id}/update/`
- **Method:** `PATCH`
- **Description:** Allows the manager to update the rejected feedback.
- **Access:** Admins and Managers only.

#### Request Body:

```json
{
  "feedback": "The feedback has been updated after revision."
}
```

#### Response:

```json
{
  "id": 1,
  "feedback": "The feedback has been updated after revision.",
  "stage": "Feedback Provided"
}
```

---

## Permissions

Permissions control access to the various endpoints:

1. **IsAdminOrManager**:
  - Admins have full access to all endpoints.
  - Managers can view and modify records, but they cannot delete them.
  - Employees can view their own performance reviews but cannot modify or delete them.
  - Unauthenticated users have no access.

---

## Notes

1. Replace `{id}` in the endpoints with the actual ID of the company, department, or performance review.
2. Ensure JWT tokens are included in the request headers for authenticated requests.
3. Permissions are enforced to restrict access based on roles.
4. All transitions between review stages must follow the defined workflow.