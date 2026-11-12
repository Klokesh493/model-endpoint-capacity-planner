# Model Endpoint Capacity Planner

Serving teams need to translate forecast requests into replica counts while reserving headroom for demand variation.

## What I built

I built a replica sizing calculator that applies headroom to target QPS, divides by measured per-replica QPS, and rounds up to a minimum of one replica.

## How it works

```mermaid
flowchart LR
    A["Target QPS, replica throughput, and headroom"]
    B["Scale target by headroom"]
    C["Divide by replica throughput and round up"]
    D["Recommended replica count with minimum of one"]
    A --> B --> C --> D
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [capacity_planner.py](capacity_planner.py) implements the CLI and decision rules. Uses `csv` to read tabular exports, `math` to compute numeric estimates. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 capacity_planner.py sample_capacity.csv
```

The fixture recommends 10 replicas for ranker and two for classifier. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 capacity_planner.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

Use throughput measured at the required latency target. Check cold starts, load variability, and downstream limits separately.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
