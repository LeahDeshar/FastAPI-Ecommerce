### Operations and API Endpoints

#### 4. **Cart Management Service**

| Operation                     | API Endpoint             | Description                                       |
| ----------------------------- | ------------------------ | ------------------------------------------------- |
| **Add Item to Cart**          | `POST /cart`             | Adds a product to the user's cart.                |
| **View Cart**                 | `GET /cart`              | Retrieves all items currently in the user's cart. |
| **Update Cart Item Quantity** | `PUT /cart/{item_id}`    | Updates the quantity of a product in the cart.    |
| **Remove Item from Cart**     | `DELETE /cart/{item_id}` | Removes a specific item from the user's cart.     |
