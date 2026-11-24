"""Core Telemetry Profiler implementation."""
from typing import Dict, List, Any

class StepMetric:
    def __init__(self, step_name: str, prompt_tokens: int, completion_tokens: int, duration_ms: float, cost_dollars: float):
        self.step_name = step_name
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.duration_ms = duration_ms
        self.cost_dollars = cost_dollars

class TelemetryProfiler:
    # Standard 2026 model pricing ($ per 1M tokens)
    PROMPT_COST_PER_M = 1.50
    COMPLETION_COST_PER_M = 6.00

    def __init__(self):
        self.steps: List[StepMetric] = []

    def log_step(self, step_name: str, prompt_tokens: int, completion_tokens: int, duration_ms: float) -> StepMetric:
        cost = (prompt_tokens * self.PROMPT_COST_PER_M / 1_000_000.0) + (completion_tokens * self.COMPLETION_COST_PER_M / 1_000_000.0)
        metric = StepMetric(step_name, prompt_tokens, completion_tokens, duration_ms, round(cost, 6))
        self.steps.append(metric)
        return metric

    def get_summary(self) -> Dict[str, Any]:
        tot_prompt = sum(s.prompt_tokens for s in self.steps)
        tot_comp = sum(s.completion_tokens for s in self.steps)
        tot_dur = sum(s.duration_ms for s in self.steps)
        tot_cost = sum(s.cost_dollars for s in self.steps)

        return {
            "total_steps": len(self.steps),
            "total_tokens": tot_prompt + tot_comp,
            "total_duration_ms": round(tot_dur, 2),
            "total_cost_dollars": round(tot_cost, 6),
            "most_expensive_step": max(self.steps, key=lambda s: s.cost_dollars).step_name if self.steps else None
        }
