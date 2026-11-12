# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 capacity_planner.py sample_capacity.csv
ranker 10
classifier 2
test_calculates_replicas_with_headroom (test_capacity_planner.CapacityPlannerTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
