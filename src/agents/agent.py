import random
import math

class Agent:
    def __init__(self, identity, cash, holdings, risk_tolerance, PnL_memory = 0):
        self.id = identity
        self.cash = cash
        self.holdings = holdings
        self.risk_tolerance = risk_tolerance # -----> Between 0 and 1 ----> float
        self.pNl = PnL_memory # ------> floating point and pNl percentage 

    def action(self, current_price, price_movement):
        tendency = self.tendency(price_movement)
        buy_prob  = max(0, tendency)
        sell_prob = max(0, -tendency)
        hold_prob = 1 - buy_prob - sell_prob 

        act = random.choices([1,-1,0], weights=[buy_prob, sell_prob, hold_prob])[0]
        vol = self.volume(act, current_price, price_movement)
        return(act, vol)


    def volume(self, act, current_price, price_movement):
        conviction = abs(self.tendency(price_movement))
        noise = random.uniform(-0.3,0.3)
        if (conviction * self.risk_tolerance <= 0.3) :
            noise = abs(noise) 
        trade_fraction = conviction * self.risk_tolerance + noise
        budget = self.cash * trade_fraction
        buy_vol = budget // current_price
        sell_vol = trade_fraction * self.holdings

        if(act == 1):
            return buy_vol
        else:
            return sell_vol

    def tendency(self, price_movement):
        noise = random.uniform(-0.2,0.2)
        pNl_adjusted = 0.4 * math.tanh(self.pNl) # Capping pNl so it doesn't over influence
        tendency = price_movement + pNl_adjusted + noise
        adjusted_tendency = tendency * self.risk_tolerance
        adjusted_tendency = adjusted_tendency = math.tanh(adjusted_tendency)
        return adjusted_tendency
    



    
