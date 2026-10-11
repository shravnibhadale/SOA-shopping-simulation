# SOA-Based Shopping Simulation on AWS EC2

A simple shopping application simulation built using **Service-Oriented Architecture (SOA)** and deployed on an **AWS EC2 Linux instance**. The project demonstrates how independent services communicate through REST APIs to process an order, simulate payment, and send an order confirmation.

## Project Overview

This project demonstrates the relationship between SOA and cloud computing by dividing a shopping workflow into three independent services. Each service performs a specific task and communicates with other services through HTTP requests.

The application also demonstrates error handling and service recovery when a dependent service becomes unavailable.

## Architecture

The application consists of three Flask microservices:

1. **Order Service** – Receives an order request and coordinates the shopping workflow.
2. **Payment Service** – Simulates payment processing and returns the payment status.
3. **Notification Service** – Simulates sending an order confirmation.

### Workflow

```text
                  User
                   |
                   v
             Order Service
                   |
             +-----+------+
             |            |
             v            v
       Payment Service  Notification Service
             |            |
             v            v
       Payment Status  Notification Status
             |            |
             +------+-----+
                    |
                    v
             Order Response
```

## Technologies Used

- **Cloud Platform:** Amazon Web Services (AWS)
- **Compute Service:** Amazon EC2
- **Operating System:** Amazon Linux 2023
- **Programming Language:** Python
- **Framework:** Flask
- **Communication:** REST APIs over HTTP
- **Version Control:** Git and GitHub

## Project Structure

```text
soa-shopping/
├── order_service/
│   └── app.py
├── payment_service/
│   └── app.py
├── notification_service/
│   └── app.py
├── README.md
├── architecture.md
├── requirements.txt
└── .gitignore
```

## Service Endpoints

| Service | Port | Endpoint |
|---|---:|---|
| Order Service | 5001 | `/order` |
| Payment Service | 5002 | `/pay` |
| Notification Service | 5003 | `/notify` |

The Order Service also provides a basic web page at `/`.

## How It Works

1. The user initiates an order through the Order Service.
2. The Order Service sends a request to the Payment Service.
3. The Payment Service simulates a successful payment and returns its status.
4. The Order Service contacts the Notification Service.
5. The Notification Service simulates sending an order confirmation.
6. The Order Service returns the combined order, payment, and notification statuses.

## Installation and Setup

### Prerequisites

- Python 3
- pip
- An AWS EC2 Linux instance or another Linux environment
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/shravnibhadale/SOA-shopping-simulation.git
cd SOA-shopping-simulation
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Start the services

Open separate terminal sessions in the project directory.

**Terminal 1 — Payment Service**

```bash
python3 payment_service/app.py
```

**Terminal 2 — Notification Service**

```bash
python3 notification_service/app.py
```

**Terminal 3 — Order Service**

```bash
python3 order_service/app.py
```

Ensure that each service is configured to listen on its intended port and that the service URLs match the environment in which the application is running.

### 4. Test the application

On the same machine, send a request to the Order Service:

```bash
curl http://127.0.0.1:5001/order
```

A successful response should contain an order status of `CREATED`, a payment status of `SUCCESS`, and a notification status of `SENT`.

The exact response depends on the service implementation and its current state.

## Failure Handling and Recovery

A failure-recovery test was performed to demonstrate service dependency handling.

**Test procedure:**

1. Stop the Payment Service.
2. Send a request to the Order Service.
3. Observe the failed order response when the dependent service is unavailable.
4. Restart the Payment Service.
5. Send the request again and verify that the workflow succeeds.

**Expected results:**

- When the Payment Service is unavailable, the Order Service returns an error response with the order status `FAILED`.
- After the Payment Service is restored, the order workflow succeeds again.

This test demonstrates basic fault handling and recovery in a distributed application.

## Relationship Between SOA and Cloud Computing

**Service-Oriented Architecture (SOA)** structures an application as independent services that communicate through defined interfaces.

**Cloud computing** provides on-demand infrastructure to deploy and run applications.

In this project:

- SOA is demonstrated through the separation of order, payment, and notification responsibilities.
- REST APIs enable communication between services.
- AWS EC2 provides the virtual server on which the services run.
- Service failure and recovery demonstrate the importance of handling dependencies in distributed applications.

## Learning Outcomes

- Understanding the fundamentals of SOA.
- Creating REST APIs using Flask.
- Implementing communication between independent services.
- Deploying a Python application on AWS EC2.
- Testing service availability and handling dependency failures.
- Understanding the role of cloud infrastructure in application deployment.

## Future Enhancements

- Add a real database to store orders.
- Implement a frontend shopping interface.
- Containerize each service using Docker.
- Configure Nginx as a reverse proxy.
- Implement centralized monitoring and logging.
- Automate deployment using Jenkins CI/CD.
- Add authentication and secure service communication.

## Author

**Shravni Bhadale**

GitHub: [@shravnibhadale](https://github.com/shravnibhadale)

---

*This project was developed for academic learning to demonstrate Service-Oriented Architecture and its relationship with cloud computing using AWS EC2.*
