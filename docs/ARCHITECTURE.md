# Model Endpoint Capacity Planner architecture

Estimates replicas needed for model serving from QPS, latency budget, and per-replica throughput.

```mermaid
flowchart LR
    A["Target QPS, replica throughput, and headroom"]
    B["Scale target by headroom"]
    C["Divide by replica throughput and round up"]
    D["Recommended replica count with minimum of one"]
    A --> B --> C --> D
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
