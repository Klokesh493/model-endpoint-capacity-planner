# Model Endpoint Capacity Planner architecture

Estimates replicas needed for model serving from QPS, latency budget, and per-replica throughput.

```mermaid
flowchart LR
    N0["sample_capacity.csv"]
    N1["capacity_planner.py"]
    N2["replicas needed"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
