"""Tests for TelemetryProfiler."""
import unittest
from agent_step_cost_telemetry_profiler.core import TelemetryProfiler

class TestTelemetryProfiler(unittest.TestCase):
    def test_cost_calculation(self):
        prof = TelemetryProfiler()
        m = prof.log_step("step1", 1_000_000, 0, 100.0)
        self.assertAlmostEqual(m.cost_dollars, 1.50, places=2)

        summary = prof.get_summary()
        self.assertEqual(summary["total_steps"], 1)
        self.assertEqual(summary["most_expensive_step"], "step1")
