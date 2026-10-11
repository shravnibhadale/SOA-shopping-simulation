# SOA Online Shopping Architecture

```mermaid
flowchart TD
    A[Client] --> B[Order Service :5001]
    B -->|HTTP Request| C[Payment Service :5002]
    B -->|HTTP Request| D[Notification Service :5003]
    C --> E[Payment Result]
    D --> F[Notification Result]
    E --> B
    F --> B
    B --> G[Combined Order Response]

This diagram shows how the services communicate. The ports are internal to the EC2 instance.

## Step 25: Understand the workflow

<box border radius="lg" padding={3} gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" size="42px" align="center" justify="center">
      <icon name="shopping-cart" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **1. Client requests an order**

      <text color="secondary" size="sm">The client calls the Order Service API.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" size="42px" align="center" justify="center">
      <icon name="credit-card" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **2. Payment Service responds**

      <text color="secondary" size="sm">The Order Service sends an HTTP request to simulate payment.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" size="42px" align="center" justify="center">
      <icon name="bell" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **3. Notification Service responds**

      <text color="secondary" size="sm">It simulates an order confirmation.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="md" size="42px" align="center" justify="center">
      <icon name="check-circle" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **4. Combined response**

      <text color="secondary" size="sm">The Order Service returns the results from both services.</text>
    </box>
  </row>
</box>

## Step 26: Document the SOA concept

Run:

```bash
cat >> ~/soa-shopping/README.md <<'EOF'

## SOA Concepts Demonstrated
- Separation of responsibilities across services.
- Communication using HTTP APIs.
- Each service has its own endpoint.
- The Order Service coordinates the workflow.

## Cloud Computing
The services run on an AWS EC2 virtual machine.
EC2 provides the compute infrastructure; SOA describes how
the application is divided into communicating services.
