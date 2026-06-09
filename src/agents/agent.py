import random
import math

class Agent:
    def __init__(self, identity, cash, holdings, risk_tolerance, PnL_memory = None, tendency_value = 0):
        self.id = identity
        self.cash = cash
        self.holdings = holdings
        self.risk_tolerance = risk_tolerance # -----> Between 0 and 1 ----> float
        self.pNl = PnL_memory if PnL_memory is not None else [0,]# ------> floating point and pNl percentage 
        self.tendency_val = tendency_value
        self.agent_history = []
        self.wealth = 0


    def action(self, current_price, price_movement):
        self.tendency(price_movement) # calling this to make sure no stale value

        buy_prob  = max(0, self.tendency_val)
        sell_prob = max(0, -self.tendency_val)
        hold_prob = 1 - buy_prob - sell_prob 

        hold_prob = max(0, hold_prob)

        act = random.choices([1,-1,0], weights=[buy_prob, sell_prob, hold_prob])[0]
        vol = self.volume(act, current_price)

        self.wealth = self.cash + self.holdings * current_price
        return(act, vol)


    def volume(self, act, current_price):
        conviction = abs(self.tendency_val)
        noise = random.uniform(-0.3,0.3)
        if (conviction * self.risk_tolerance <= 0.3) : 
            noise = abs(noise)  # Fomo increases whenn conviction is very less and only upward noise remains...  
        trade_fraction = conviction * self.risk_tolerance + noise 
        trade_fraction = abs(math.tanh(trade_fraction))

        budget = self.cash * trade_fraction
        buy_vol = budget // current_price
        sell_vol = int(trade_fraction * self.holdings)

        if act == 1:
            return buy_vol
        elif act == -1:
            return sell_vol
        else:
            return 0

    def tendency(self, price_movement):
        noise = random.uniform(-0.2,0.2) 
        pNl_adjusted = 0.4 * math.tanh(self.pNl[-1]) # Capping pNl so it doesn't over influence and only letting it see the last pNl
        tendency = price_movement + pNl_adjusted + noise
        adjusted_tendency = tendency * self.risk_tolerance
        adjusted_tendency = math.tanh(adjusted_tendency)
        self.tendency_val = adjusted_tendency
    
    def update_values(self, current_price, act, vol ):
        
        if act == -1:
            self.holdings -= vol
            self.cash += vol * current_price
            
        else :
            self.cash -= vol * current_price
            self.cash = max(0,self.cash)
            self.holdings +=  vol

        updated_wealth = current_price * self.holdings + self.cash
        updated_pnl = (self.wealth - updated_wealth) / self.wealth
        self.wealth = updated_wealth
        self.pNl.append(updated_pnl)
        

    def cash_effect(self, current_price):
        possible_buys = math.tanh(math.tanh(self.cash// current_price))
        pass
        # on hold.. cann't figure out what to do about money and accounting..
    
    def log_tick(self, tick, price, act, vol):
        wealth = self.cash + self.holdings * price

        self.agent_history.append({
            "tick": tick,
            "agent_id": self.id,
            "price": price,
            "wealth": wealth,
            "cash": self.cash,
            "holdings": self.holdings,
            "tendency": self.tendency_val,
            "action": act,
            "volume": vol,
            "pnl": self.pNl[-1]
        })


class MomentumTrader(Agent):

    def __init__(self, identity, cash, holdings, risk_tolerance, PnL_memory=None, tendency_value=0):
        super().__init__(identity, cash, holdings, risk_tolerance, PnL_memory, tendency_value)
        self.lookback = 0

    def tendency(self, price_movement):
        noise = random.uniform(-0.2,0.2)
        pnl_adjusted = 0
        l = self.lookback
         # to create some randomness amonng Momentumtraders too
        for i in range(1,l+1):
            pnl_adjusted += self.pNl[-i]
        pnl_adjusted = math.tanh(pnl_adjusted) # ----between 0 and 1 

        new_tendency = 1.7 * price_movement + pnl_adjusted + noise
        adjusted_tendency = math.tanh(new_tendency) 

        self.tendency_val = adjusted_tendency

    def lookback(self):    # Call once at the start in the notebook
        
        if len(self.pNl) < 7 : 
            self.lookback = 1
        elif len(self.pNl) < 15:
            self.lookback = 3
        else:
            self.lookback = 5 + random.choice([-1,-2,2,4,6])







    
