# Core Architecture  
  
## 1. Agent Layer  
  
src/agents 

The agent layer defines market participants.

Each agent maintains:

- cash
- asset holdings
- behavioral parameters
- risk preferences
- decision logic

Agents observe the market state and decide whether to:

- buy
- sell
- hold

Future versions may include:

- adaptive confidence
- memory systems
- imitation behavior
- leverage
- strategy evolution
- network interactions

---

## 2. Market Layer

Location:

```
src/market/
```

The market layer aggregates agent behavior into price movement.

Core responsibilities:

- collecting orders
- measuring imbalance
- updating prices
- recording market state

The current market mechanism assumes:

- excess buying pressure pushes prices upward
- excess selling pressure pushes prices downward

Future versions may include:

- liquidity depth
- slippage
- nonlinear impact
- order books
- volatility-sensitive pricing

---

## 3. Simulation Engine

Location:

```
src/simulation/
```

The simulation engine controls timestep progression.

Each timestep currently follows:

1. agents observe market conditions
2. agents generate actions
3. market aggregates actions
4. price updates
5. state is recorded

This ordering is extremely important for maintaining consistent causal dynamics.

---

## 4. Analytics Layer

Location:

```
src/analysis/
```

The analytics layer studies emergent market behavior.

Planned measurements include:

- volatility
- drawdowns
- wealth concentration
- imbalance persistence
- regime transitions
- return distributions

The goal is to compare simulated behavior with known stylized facts of financial markets.

---

## 5. Visualization Layer

The visualization layer transforms simulation output into interpretable visual systems.

Planned visualizations include:

- price evolution
- volatility regimes
- wealth distributions
- liquidity stress
- behavioral participation
- regime transitions

Visualization is considered essential because emergent systems are often better understood visually than numerically.

---

# Design Principles

## Modularity

Each component should remain separable and independently extendable.

The system should support adding new:

- agent types
- market structures
- pricing mechanisms
- behavioral rules

without restructuring the entire codebase.

---

## Interpretability

The simulator prioritizes understandable mechanisms over extreme realism.

The objective is to explain:

- why behaviors emerge
- what assumptions create instability
- how interactions shape outcomes

---

## Reproducibility

Experiments should eventually become reproducible through:

- fixed seeds
- scenario presets
- parameter configuration systems

---

## Extensibility

The architecture is intentionally designed for long-term expansion toward:

- derivatives integration
- stochastic modeling
- adaptive learning systems
- market microstructure
- systemic risk analysis