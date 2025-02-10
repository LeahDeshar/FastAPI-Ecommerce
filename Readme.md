# Ecommerce API with FastAPI and SQLite - Microservice Architecture

Ecommerce web app using FastAPI and SQLite, with a microservice architecture. It handles user authentication, product management, cart management, order processing, and payment integration. Modular services ensure flexibility and easy maintenance.

## Technologies for Integration

- FastAPI for the backend.
- JWT for authentication.
- SQLite for databases
- Docker to containerize each microservice.
- Redis for caching and message queues.
- Nginx as a reverse proxy for routing requests.

---

## SERVICES

### 1. **Authentication**

- **Responsibilities**: Manages user login, registration, and authentication via JWT tokens.
- **Key Features**:
  - [x] User registration
  - [x] User login
  - [x] JWT token generation
  - [x] Role-based authentication
  - [x] Token validation
  - [ ] Secure user profile access

### 2. **User Management**

- **Responsibilities**: Handles CRUD operations for user profiles and user-related data.
- **Key Features**:
  - [ ] Manage user profiles (retrieve, update, delete user details)
  - [ ] Manage user account settings
  - [ ] Role and permission management

### 3. **Product Management Service**

- **Responsibilities**: Manages product listings, product details, and product inventory.
- **Key Features**:
  - [ ] Add new products (Admin only)
  - [ ] Update product details (Admin only)
  - [ ] List all products
  - [ ] Get details of specific products
  - [ ] Search for products
  - [ ] Delete products (Admin only)

### 4. **Cart Management Service**

- **Responsibilities**: Manages users' shopping cart, including adding/removing products and updating item quantities.
- **Key Features**:
  - [ ] Add items to cart
  - [ ] View current cart
  - [ ] Update item quantities in cart
  - [ ] Remove items from cart

### 5. **Order Management Service**

- **Responsibilities**: Handles the creation and management of orders, including order history and status updates.
- **Key Features**:
  - [ ] Create new orders
  - [ ] View order history for a user
  - [ ] View details of a specific order
  - [ ] Update order status (Admin only)

### 6. **Payment Service**

- **Responsibilities**: Manages payment initiation, payment status, and updating payment information.
- **Key Features**:
  - [ ] Initiate payments for orders
  - [ ] Check payment status
  - [ ] Update payment details (Admin only)

### 7. **Admin Service**

- **Responsibilities**: Provides admin-level functionalities, such as managing users, products, orders, and viewing system statistics.
- **Key Features**:
  - [ ] View and manage user profiles
  - [ ] View and manage products
  - [ ] View and manage orders
  - [ ] View system stats (e.g., total sales, number of users)

---
