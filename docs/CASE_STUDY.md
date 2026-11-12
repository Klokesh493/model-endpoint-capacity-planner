# Model Endpoint Capacity Planner walkthrough

## Business problem

Estimates replicas needed for model serving from QPS, latency budget, and per-replica throughput.

## Reproduce the workflow

Run `python3 capacity_planner.py sample_capacity.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
ranker 10
classifier 2
```

The sample supplies these fields. `model`, `target_qps`, `per_replica_qps`, `headroom`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
