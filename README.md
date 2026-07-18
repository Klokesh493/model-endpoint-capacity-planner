# Model Endpoint Capacity Planner

Estimates replicas needed for model serving from QPS, latency budget, and per-replica throughput.

Focus: AI/ML platform capacity.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 capacity_planner.py sample_capacity.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```
