docs/journal/

This is:
your chronological thinking.

Contains:

what happened
what failed
what confused you

This becomes:
your “lab notebook.”

docs/research/

This is:
higher-level insight accumulation.

NOT daily stuff.

Contains:

observations
hypotheses
future experiments
interesting questions

This becomes:
your “thinking layer.”

docs/system_design/

ONLY:
“How is the system structured?”

This is where:

agent architecture
assumptions
market mechanics

live.

Keeps technical design separate from experimentation.

VERY important.

----
STEP 3 — NOTEBOOK STRUCTURE TEMPLATE

Every notebook should now follow the SAME pattern.

This becomes your lab workflow.

At TOP of notebook:

EXPERIMENT_ID = "momentum_v1"

EXPERIMENT_GOAL = """
Test whether momentum-based agents generate persistent trends
and different imbalance dynamics compared to baseline agents.
"""

VERY important habit.

Then:

SECTION 1 — Imports
from src.market import Market
from src.agents import Agent, MomentumTrader
from src.simulation import run_simulation
SECTION 2 — Experiment Parameters

ONLY parameters.

Example:

NUM_AGENTS = 100
MOMENTUM_RATIO = 0.3
STEPS = 600
SENSITIVITY = 0.08

This becomes EXTREMELY useful later.

SECTION 3 — Run Experiment

Clean.
Minimal.

SECTION 4 — Visualization

Plots only.

SECTION 5 — Observations

Markdown section:

# Observations

Then:

what happened
what surprised you
bugs discovered
assumptions challenged

THIS is the intellectual core.

STEP 4 — SAVE PLOTS AUTOMATICALLY

VERY important.

After every important plot:

plt.savefig("plots/momentum/momentum_v1_price.png")

DO THIS ALWAYS.

Otherwise:
you WILL lose meaningful results later.

Trust me 😭

STEP 5 — CREATE EXPERIMENT NAMING CONVENTION

This matters A LOT later.

Good format:

momentum_v1
momentum_v2
liquidity_debug_v1
pricing_fix_v1

NOT:

final_final2_fixed_REAL.ipynb

😭

STEP 6 — CREATE TWO IMPORTANT NOTE FILES
notes/observations.md

ONLY insights.

Example:

# Momentum Experiment

- Momentum agents increased imbalance spikes.
- Market exhibited stronger local volatility bursts.
- Pricing equation accidentally created bullish drift.

SHORT.

Not essays.

notes/failures.md

This is GOLD.

Example:

# Failure — Return Squaring

Problem:
Squaring returns removed sign information.

Effect:
Negative returns became positive,
creating unintended upward drift.

This file becomes:

blog material
interview material
learning material

VERY valuable.

STEP 7 — GIT WORKFLOW

After EVERY meaningful experiment:

git add .
git commit -m "Ran first momentum trader market experiment"

NOT every tiny typo.

Only meaningful milestones.

STEP 8 — WHEN TO CREATE NEW NOTEBOOKS

IMPORTANT RULE:

Create NEW notebook when:
research question changes
architecture changes substantially
experiment purpose changes

Examples:

✅ baseline market
✅ momentum agents
✅ liquidity debugging
✅ volatility clustering

DO NOT create new notebook for:
tiny bug fixes
plot adjustments
parameter tweaks

That becomes chaos.

STEP 9 — WHAT TO PRESERVE VS CURATE

Preserve EVERYTHING privately.

Curate selectively publicly.

This is VERY important.

Your repo/blog should NOT become:
“500 random plots.”

Instead:

strongest experiments
key failures
important transitions
meaningful observations

That’s the storytelling layer.