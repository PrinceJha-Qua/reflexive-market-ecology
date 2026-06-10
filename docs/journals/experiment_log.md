# Day 1 — First Living Market  
  
## Objective  
  
Build the smallest possible agent-driven market simulation.  
  
---  
  
## Implemented  
  
- primitive agent structure  
- buy/sell/hold actions  
- volume generation  
- market imbalance aggregation  
- price update mechanism  
- simulation loop  
- historical state recording  
- first visualizations  
  
---  
  
## Initial Observations  
  
The market now produces price movement through aggregate agent behavior rather than pure random walk generation.  
  
The first complete feedback loop now exists:  
  
Agents → Actions → Imbalance → Price Change → New Decisions  
  
This is the foundational mechanism for all future emergent behavior.  
  
---  
  
## Interesting Behaviors  
  
- price remained bounded instead of exploding  
- aggregate imbalance visibly affected returns  
- risk tolerance already creates behavioral divergence  
- different runs produce noticeably different trajectories  
  
---  
  
## Problems Observed  
  
- behavior still feels highly mechanical  
- randomness dominates too strongly  
- agents lack persistent identity over time  
- no long-term memory exists yet  
- price dynamics remain too smooth and linear  
  
---  
  
## Key Insight  
  
Even extremely primitive behavioral rules are capable of generating nontrivial market movement once interaction and feedback are introduced.  
  
The project is beginning to feel less like a static model and more like an evolving system.  
  
---  
  
# Planned Next Steps  
  
- stronger behavioral heterogeneity  
- persistent agent personalities  
- richer market metrics  
- nonlinear market response  
- reflexive feedback mechanisms


## Day 4
- So today I ended up adding the Momentum Trader Behavioral Subclass within the Agent Class which was much more neutral. It was previously actig on just random numerical differences between the Agents. Now I have tried to add concrete bbehavioral differences between the Agents by itroducing different type of Market players. I am starting with MomentumTrader and this experimet is done to obseve and understand those difference. 

### Observation - Behavioral Heterogeneity

Introducing MomentumTrader agents altered aggregate market behavior despite the pricing mechanism remaining unchanged.

The momentum-heavy market exhibited:

larger imbalance spikes
more volatile return bursts
different long-term price evolution

This was my first direct observation of emergent behavior arising from local decision rules

# Simulation Debugging Notes : Emergent Market Behavior

## Observation 1 : Buy/Sell Pressure Asymmetry

During the first simulation runs, buy pressure consistently dominated sell pressure numerically.

After inspection, I realized buy and sell volumes were being generated using fundamentally different scales:

* buy volume depended on cash/current_price
* sell volume depended only on holdings fraction

This unintentionally created structurally stronger buying pressure.

### Insight

Small implementation asymmetries can create persistent macro-level market bias.

---

## Observation 2 : Accidental Bullish Drift

The pricing function applied:

```python
returns = returns * returns
```

for small returns.

This removed directional sign information, causing negative returns to become positive.

As a result:
even bearish imbalance contributed upward price movement.

### Insight

Nonlinear transformations can unintentionally destroy critical behavioral information in simulations.

---

## Observation 3 : Behavioral Heterogeneity Produced Different Dynamics

Introducing MomentumTrader agents changed:

* imbalance structure
* return volatility
* aggregate price evolution

despite the pricing mechanism remaining identical.

### Insight

Local behavioral rules can propagate into visibly different macro market dynamics.

This was my first direct experience observing emergent behavior in a market simulation.

---

## Observation 4 : Architecture Validation

The subclass-based architecture successfully allowed behavioral modification without rewriting market mechanics.

Only `tendency()` needed overriding for MomentumTrader agents.

### Insight

Separating market mechanics from behavioral interpretation created a clean extensible simulation structure.





----
Phase 2 : 

Experimental Results - Phase 2
Experiment A

Risk Tolerance Sweep

30 simulations per risk level.

Risk Levels:

0.2
0.4
0.6
0.8

Initial Hypothesis

Higher risk tolerance should increase volatility.

Result

Opposite outcome observed.

Higher risk tolerance produced:

Higher trading volume
Lower volatility
Additional Investigations

Measured:

Synchronization
Conviction
Volume
Imbalance
Findings

Synchronization increased with risk.

Conviction increased with risk.

Trading volume increased strongly with risk.

However:

Higher volume corresponded to lower average absolute returns.

Liquidity Effect

Observed relationship:

Higher Risk
→ Higher Participation
→ Higher Volume
→ Smaller Imbalances
→ Lower Volatility

Conclusion

Within the current market ecology:

Risk tolerance behaves more like a liquidity parameter than a volatility parameter.

Experiment B

Normal vs Momentum Populations

Configurations:

100 Normal
50 Normal / 50 Momentum
100 Momentum
Observation

Pure momentum populations frequently underperformed mixed populations.

Repeated pattern:

Early upward movement followed by prolonged decay.

Possible Explanation

Momentum agents amplify existing trends.

Combined with fear asymmetry:

Negative moves become self-reinforcing.

Interesting Observation

Mixed populations often produced the most stable outcomes.

Potential indication that behavioral diversity improves market stability.
