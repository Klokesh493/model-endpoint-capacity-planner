import csv
import math
import sys


def replicas_needed(row):
    target_qps = float(row["target_qps"])
    per_replica_qps = float(row["per_replica_qps"])
    headroom = float(row.get("headroom", 1.3))
    return max(1, math.ceil(target_qps * headroom / per_replica_qps))


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['model']} {replicas_needed(row)}")


if __name__ == "__main__":
    main(sys.argv[1])
