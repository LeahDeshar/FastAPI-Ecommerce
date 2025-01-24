### Operations and API Endpoints

#### 3. **Product Management Service**

| Operation               | API Endpoint                    | Description                                                |
| ----------------------- | ------------------------------- | ---------------------------------------------------------- |
| **Add New Product**     | `POST /products`                | Admin-only endpoint to add new products to the inventory.  |
| **List All Products**   | `GET /products`                 | Retrieves all products in the catalog.                     |
| **Get Product Details** | `GET /products/{product_id}`    | Retrieves detailed information for a single product by ID. |
| **Update Product**      | `PUT /products/{product_id}`    | Admin-only endpoint to update an existing product.         |
| **Delete Product**      | `DELETE /products/{product_id}` | Admin-only endpoint to remove a product from the catalog.  |
