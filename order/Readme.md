### Operations and API Endpoints

#### 5. **Order Management Service**

| Operation                      | API Endpoint             | Description                                                                           |
| ------------------------------ | ------------------------ | ------------------------------------------------------------------------------------- |
| **Create Order**               | `POST /orders`           | Places a new order for the items in the user's cart.                                  |
| **Get User Order History**     | `GET /orders`            | Retrieves a history of orders placed by the authenticated user.                       |
| **Get Specific Order Details** | `GET /orders/{order_id}` | Retrieves detailed information about a specific order by ID.                          |
| **Update Order Status**        | `PUT /orders/{order_id}` | Admin-only operation to update the status of an order (e.g., pending, shipped, etc.). |
