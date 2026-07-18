import unittest

from capacity_planner import replicas_needed


class CapacityPlannerTest(unittest.TestCase):
    def test_calculates_replicas_with_headroom(self):
        row = {"model": "ranker", "target_qps": "900", "per_replica_qps": "120", "headroom": "1.3"}
        self.assertEqual(replicas_needed(row), 10)


if __name__ == "__main__":
    unittest.main()
