## Purpose  
  
This document tracks the simplifying assumptions used throughout the simulator.  
  
The objective is not perfect realism, but interpretable experimentation.  
  
Making assumptions explicit is important because small modeling choices can significantly alter emergent system behavior.  
  
---  
  
# Current Assumptions  
  
## Single Asset Market  
  
The simulator currently models only one tradable asset.  
  
Cross-asset effects and portfolio interactions are ignored for simplicity.  
  
---  
  
## Centralized Market Price  
  
The market currently maintains a single global price shared by all participants.  
  
No bid-ask spread or fragmented pricing exists yet.  
  
---  
  
## Imbalance-Driven Pricing  
  
Price movement is generated through aggregate order imbalance.  
  
More buying pressure increases price.  
More selling pressure decreases price.  
  
The current implementation assumes a simplified direct relationship between imbalance and price impact.  
  
---  
  
## Local Information  
  
Agents currently observe only limited market information:  
- current price  
- recent price movement  
  
No external news or macroeconomic variables exist yet.  
  
---  
  
## No Transaction Costs  
  
Trading currently occurs without:  
- commissions  
- slippage  
- latency  
- market impact costs  
  
These may be introduced later.  
  
---  
  
## No Leverage  
  
Agents currently trade only with available cash and holdings.  
  
Borrowing and margin dynamics do not yet exist.  
  
---  
  
## Primitive Behavioral Logic  
  
Current agent behavior is intentionally simple.  
  
The purpose of early phases is to study how complexity can emerge from minimal rules before introducing richer psychology.  
  
---  
  
# Philosophy of Simplification  
  
This simulator intentionally sacrifices realism in order to preserve interpretability.  
  
The objective is not to replicate real markets exactly, but to understand how behavioral interaction and feedback can generate complex dynamics.