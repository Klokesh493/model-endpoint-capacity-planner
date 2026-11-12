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

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

```mermaid
flowchart LR
    A["Target QPS, replica throughput, and headroom"]
    B["Scale target by headroom"]
    C["Divide by replica throughput and round up"]
    D["Recommended replica count with minimum of one"]
    A --> B --> C --> D
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
