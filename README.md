# Market Ecology

*A first-principles exploration of how markets emerge from interacting agents.*

---

## Overview

Market Ecology is an ongoing agent-based market simulation project that attempts to study market behavior from the bottom up.

Instead of beginning with established financial models, this project starts with a simpler question:

> How much market complexity can emerge from a collection of simple interacting agents?

The simulator is being built incrementally from scratch, with every assumption, experiment, bug, and architectural decision documented along the way.

The objective is not to perfectly replicate real financial markets.

The objective is to understand how interaction, feedback loops, memory, incentives, and behavioral diversity produce larger system-level phenomena.

---

## Project Philosophy

Most market models begin with sophisticated assumptions.

This project intentionally does the opposite.

The approach is:

1. Start with the simplest possible market.
2. Introduce one mechanism at a time.
3. Observe emergent behavior.
4. Challenge assumptions.
5. Iterate.

Rather than immediately reproducing existing market ecology frameworks, the project explores the design space independently and treats mistakes as part of the research process.

Many of the most important insights have emerged from debugging incorrect assumptions rather than implementing successful features.

---

## Current Features

### Market Mechanics

* Single-asset market
* Centralized market price
* Order imbalance-based pricing
* Nonlinear price response
* Fear/optimism asymmetry experiments
* Volume-aware price impact

### Agent System

* Buy / Sell / Hold actions
* Risk tolerance heterogeneity
* Wealth tracking
* Portfolio accounting
* Profit-and-loss memory
* Behavioral logging

### Agent Types

#### Normal Agent

Baseline behavioral model driven by:

* recent price movement
* profit-and-loss feedback
* stochastic noise
* risk tolerance

#### Momentum Trader

Trend-following participant that amplifies recent market movement and incorporates historical PnL memory.

#### Contrarian Trader

Mean-reversion participant that acts against recent price movement and attempts to exploit overreaction.

---

## Research Questions

Some of the questions currently being explored:

* How does risk tolerance affect volatility?
* How does liquidity influence price stability?
* What market dynamics emerge from behavioral heterogeneity?
* Can simple feedback mechanisms generate realistic market regimes?
* How sensitive are outcomes to modeling assumptions?
* Which micro-level behaviors dominate macro-level market structure?

---

## Current Findings

Some early observations:

* Small implementation asymmetries can create large market-wide biases.
* Behavioral heterogeneity produces noticeably different market dynamics.
* Volume appears to dampen volatility rather than amplify it.
* Market outcomes are often more sensitive to assumptions than expected.
* Emergent behavior appears surprisingly early, even under primitive agent rules.

---

## Project Structure

```text
Market-Ecology/
│
├── src/
│   ├── agents/
│   ├── market/
│   ├── simulation/
│   └── analytics/
│
├── notebooks/
│
├── docs/
│   ├── journal/
│   ├── research/
│   └── system_design/
│
├── plots/
│
├── notes/
│   ├── observations.md
│   └── failures.md
│
└── README.md
```

---

## Long-Term Vision

The long-term goal extends beyond building a simulator.

One possible direction is the creation of a market experimentation framework capable of generating synthetic market scenarios.

Rare events such as:

* liquidity crises
* flash crashes
* panic cascades
* regime shifts
* market contagion

occur infrequently in reality, making them difficult to study using historical data alone.

A sufficiently rich agent-based environment could eventually serve as a laboratory for exploring such events and generating additional synthetic observations.

Whether that goal is achievable remains an open question.

Exploring that question is part of the project.

---

## Status

🚧 Active Research Project

The simulator is currently in its early development stages.

Architecture, assumptions, and agent behavior are expected to evolve significantly as experimentation continues.

---

## License

MIT License
