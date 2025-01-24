### Operations and API Endpoints

#### 6. **Payment Service**

| Operation                  | API Endpoint                 | Description                                                   |
| -------------------------- | ---------------------------- | ------------------------------------------------------------- |
| **Initiate Payment**       | `POST /payments`             | Initiates the payment process for an order.                   |
| **Get Payment Status**     | `GET /payments/{payment_id}` | Retrieves the status of a payment by payment ID.              |
| **Update Payment Details** | `PUT /payments/{payment_id}` | Admin-only operation to update payment details for a payment. |
