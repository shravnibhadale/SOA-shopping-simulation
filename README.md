## Failure Handling and Recovery Test

### Objective
To verify how the Order Service behaves when a dependent service becomes unavailable.

### Test Procedure
1. Stopped the Payment Service process.
2. Sent an order request to the Order Service.
3. Observed the failure response.
4. Restarted the Payment Service.
5. Sent the order request again and verified successful recovery.

### Results
- When Payment Service was unavailable, the Order Service returned `order_status: FAILED`.
- After restarting Payment Service, the Order Service returned `order_status: CREATED`.
- Payment Service returned `payment_status: SUCCESS`.
- Notification Service returned `notification_status: SENT`.

### Conclusion
The experiment demonstrated service-to-service API communication, dependency failure detection, and recovery after a service restart. All three services were verified on the AWS EC2 instance.


