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

## Business problem

Serving teams need to translate forecast requests into replica counts while reserving headroom for demand variation.

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

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 capacity_planner.py sample_capacity.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.
