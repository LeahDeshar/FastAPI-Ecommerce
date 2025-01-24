### 1. User Authentication

- [x] **Login and Registration**
- [x] **Get Current Users**
- [x] **JWT Authentication** (returns token)
- [ ] **Role Based Authentication and Access**

---

### Operations and API Endpoints

#### 1. **User Authentication Service**

| Operation                     | API Endpoint                  | Description                                                       |
| ----------------------------- | ----------------------------- | ----------------------------------------------------------------- |
| **Register User**             | `POST /auth/register`         | Registers a new user with email, password, and role (Admin/User). |
| **Login User**                | `POST /auth/login`            | Logs in a user and returns a JWT token for authentication.        |
| **Get Current User Profile**  | `GET /auth/profile`           | Retrieves the profile of the currently authenticated user.        |
| **Role-based Authentication** | (Integrated in all endpoints) | Based on user roles, restrict access to Admin routes.             |

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn index:app --reload
```
