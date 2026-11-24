"""CLI for Telemetry Profiler."""
import argparse
from .core import TelemetryProfiler

def main():
    parser = argparse.ArgumentParser(description="Agent Step Cost Telemetry Profiler CLI")
    parser.add_argument("--demo", action="store_true", help="Run profiler demo")
    args = parser.parse_args()

    prof = TelemetryProfiler()
    prof.log_step("Planning", 2000, 500, 420.0)
    prof.log_step("Code_Generation", 8000, 2500, 1850.0)
    prof.log_step("Verification", 1200, 200, 310.0)

    summary = prof.get_summary()
    print("Agent Workflow Telemetry Profile:")
    for k, v in summary.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
