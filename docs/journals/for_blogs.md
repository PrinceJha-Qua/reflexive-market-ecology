
Phase 2 Experiment :

Discovery 1
Volume matters differently than expected

Initially we noticed:

imbalance =
(buy-sell)/(buy+sell)

and thought:

Volume probably doesn't matter enough.

That was a reasonable concern.

Then we modified pricing:

returns =
imbalance *
sensitivity *
tanh(log(1+volume))

and ran experiments.

What happened?

Result

Higher volume markets had:

Lower average returns
Lower volatility

This was surprising.

We expected:

More volume
→ more activity
→ bigger moves

Instead:

More volume
→ more liquidity
→ smaller moves
Interpretation

You accidentally created a primitive liquidity effect.

Not because you explicitly modeled liquidity.

Because large participation naturally reduces imbalance.

This is actually a beautiful emergent property.

Discovery 2
Imbalance dominates price formation

The most revealing graph today was:

Imbalance vs Absolute Return

The relationship was almost perfectly deterministic.

Meaning:

Price Movement
≈ f(Imbalance)

Everything else:

Risk
Volume
Agent Type

only influences price indirectly through imbalance.

What this means

You now know the hierarchy:

Agent Behaviour
↓
Order Flow
↓
Imbalance
↓
Price

That hierarchy should probably be written somewhere permanently.

Because it is the architecture of the whole simulator.

Discovery 3
Fear asymmetry is already shaping the market

You introduced:

if imbalance < 0:
    imbalance *= fear_multiplier

This is no longer a tiny tweak.

It is a major structural assumption.

Because now:

Positive Imbalance
≠
Negative Imbalance

This means:

Momentum traders experience:

Positive trend
→ positive feedback

Negative trend
→ amplified positive feedback

because fear gets extra leverage.

This likely explains the slow crashes we saw.

Layer 2: What We Learned About Agents
Discovery 4
Risk tolerance is doing two jobs

Initially:

Risk Tolerance
=
Position Size

or so we thought.

After reading the code carefully:

tendency *= risk_tolerance

and

trade_fraction =
conviction * risk_tolerance

Risk affects:

Belief strength

and

Trade size

simultaneously.

Meaning:

Risk Tolerance
=
Opinion Amplifier
+
Capital Amplifier

That's important.

Because later:

Confidence

and

Risk Tolerance

might become entangled.

Discovery 5
High-risk agents are more synchronized

The synchronization plot showed:

Risk ↑
→ Synchronization ↑

This is interesting.

Not because it's huge.

But because it suggests:

Risk
→ Coordination

instead of:

Risk
→ Chaos

which was our intuition initially.

Discovery 6
High-risk agents have stronger convictions

The conviction plot was extremely clean.

Higher risk produced:

Higher Mean |Tendency|

Meaning:

Risk
=
Confidence Magnifier

within the current model.

Discovery 7
Wealth-based PnL changed everything

This is probably the biggest code-level improvement today.

Before:

Everyone learned the same lesson.

After:

Every agent learns from their own portfolio.

Now:

Good trades
Bad trades
Lucky trades

can produce different future behaviour.

This is the foundation for:

Adaptive Agents
Confidence
Evolution
Survival

later.

Layer 3: What We Learned About The Simulator

This is the really important section.

Discovery 8
The simulator is finally producing emergent behaviour

Before today:

Feature
→ Expected Outcome

Now:

Feature
→ Unexpected Outcome

Example:

Expected:
Higher Risk
→ Higher Volatility

Observed:
Higher Risk
→ Lower Volatility

That means:

You are no longer programming outputs.

You are programming rules.

The outputs are emerging.

This is the exact transition you wanted from this project.

Discovery 9
Behavioral diversity might matter

This is still preliminary.

But repeatedly:

50 Normal
50 Momentum

looked healthier than:

100 Momentum

and often competitive with:

100 Normal

Possible interpretation:

Homogeneous populations
→ Fragile

Diverse populations
→ Stable

This is literally the core idea of:

Market Ecology

which is why I think this result is worth revisiting later.