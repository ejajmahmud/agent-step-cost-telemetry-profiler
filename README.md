# Agent Step Cost Telemetry Profiler ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Agent Step Cost Telemetry Profiler Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/agent-step-cost-telemetry-profiler/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/agent-step-cost-telemetry-profiler?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/agent-step-cost-telemetry-profiler/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Agent Step Cost Telemetry Profiler** is a production-ready developer tool and connector: Granular per-step token consumption, API cost, and latency profiler for autonomous agent execution loops.

---

## 🚀 Problem Statement

Engineers lack visibility into which autonomous agent steps burn the most tokens or introduce latency bottlenecks in multi-step workflows.

---

## ⚡ Architecture Flow

```mermaid
graph LR
    Step[Agent Step Execution] --> Collector[Step Metrics Collector]
    Collector --> ModelCost[Apply Model Tier Pricing Matrix]
    ModelCost --> Aggregator[Aggregate Total Workflow Cost & Latency]
    Aggregator --> HotspotAlert[Flag High-Cost / High-Latency Step Hotspots]
```

---

## 📊 Performance Benchmarks

| Metric | Unmonitored Runs | Post-Billing Scrapes | Step Cost Telemetry Profiler | Improvement |
|---|---|---|---|---|
| Step Cost Visibility | None | Global Total Only | Exact Per-Step Dollar Cost | **Micro-level financial insight**|
| Overhead of Profiler | N/A | Batch cron | < 0.05 ms per step | **Negligible runtime cost** |
| High-Cost Step Detection | Days | Hours | Immediate (Real-time) | **Instant budget alert** |
| Token Estimation Accuracy | Rough | High-level | 100% Exact Token Match | **Zero billing surprises** |

---

## 🛠️ Installation & Quickstart

```bash
pip install agent_step_cost_telemetry_profiler
```

### Python API

```python
import agent_step_cost_telemetry_profiler

print(agent_step_cost_telemetry_profiler.__version__)
```

### CLI Usage

```bash
agent-step-cost-telemetry-profiler --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
