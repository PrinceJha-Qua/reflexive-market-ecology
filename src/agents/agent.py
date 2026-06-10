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
        self.type = "normal"


    def action(self, current_price, price_movement):
        
        self.compute_tendency(price_movement)

        action = self.choose_action()

        volume = self.volume(
            action,
            current_price
        )

        return action, volume

    def choose_action(self):

        buy_prob = max(0,self.tendency_val)

        sell_prob = max(0,-self.tendency_val)

        hold_prob = max(0,1 - buy_prob - sell_prob)

        return random.choices([1,-1,0], weights=[buy_prob,sell_prob,hold_prob])[0]


    def volume(self, act, current_price):
        conviction = abs(self.tendency_val)
        noise = random.uniform(-0.3,0.3)
        if (conviction * self.risk_tolerance <= 0.3) : 
            noise = abs(noise)  # Fomo increases whenn conviction is very less and only upward noise remains...  
        trade_fraction = conviction * self.risk_tolerance + noise 
        trade_fraction = abs(math.tanh(trade_fraction))

        buy_volume = int( (self.cash * trade_fraction)// current_price)
        sell_volume = int(trade_fraction * self.holdings)

        if act == 1:
            return buy_volume
        elif act == -1:
            return sell_volume
        return 0

    def compute_tendency(self, price_movement):
        noise = random.uniform(-0.2,0.2) 
        
        pNl_adjusted = 0.4 * math.tanh(self.pNl[-1]) # Capping pNl so it doesn't over influence and only letting it see the last pNl
        tendency = price_movement + pNl_adjusted + noise
        
        adjusted_tendency = tendency * self.risk_tolerance
        adjusted_tendency = math.tanh(adjusted_tendency)
        
        self.tendency_val = adjusted_tendency
    
    def update_values(self, current_price, act, vol ):

        if act == -1:
            vol = min(vol, self.holdings)
            self.holdings -= vol
            self.cash += vol * current_price
            
        elif act == 1 : # else has the same effect but always make distinction. Don't treat Hold as Sell = 0 and Buy = 0. 
            max_affordable = int(self.cash // current_price)
            vol = min(vol,max_affordable)
            
            self.cash -= vol * current_price
            self.cash = max(0,self.cash)
            self.holdings +=  vol
        
        self.wealth = self.cash + self.holdings * current_price

    def update_wealth(self, updated_price):

        updated_wealth = updated_price * self.holdings + self.cash
        if self.wealth <= 0: # Always remember such cases when dividing
            updated_pnl = 0
        else:
            updated_pnl = (updated_wealth - self.wealth ) / self.wealth
            self.wealth = updated_wealth
            self.pNl.append(updated_pnl)
            

    def cash_effect(self, current_price):
        possible_buys = math.tanh(math.tanh(self.cash// current_price))
        pass
        # on hold.. cann't figure out what to do about money and accounting..
    
    def log_tick(self, tick, price, act, vol):

        self.agent_history.append({
            "tick": tick,
            "agent_id": self.id,
            "type": self.type,
            "price": price,
            "wealth": self.wealth,
            "cash": self.cash,
            "holdings": self.holdings,
            "tendency": self.tendency_val,
            "action": act,
            "volume": vol,
            "pnl": self.pNl[-1]
        })


class MomentumTrader(Agent):

    def __init__(self, identity, cash, holdings, risk_tolerance, PnL_memory=None, trend_strength = 1.7, tendency_value=0):
        super().__init__(identity, cash, holdings, risk_tolerance, PnL_memory, tendency_value)
        self.lookback = random.choice([3,5,7,10])
        self.type = "momentum"
        self.trend_strength = trend_strength
        

    def compute_tendency(self, price_movement):
        noise = random.uniform(-0.2,0.2)
        pnl_adjusted = 0
        l = min(self.lookback, len(self.pNl))
         # to create some randomness amonng Momentumtraders too
        for i in range(1,l+1):
            pnl_adjusted += self.pNl[-i]
        pnl_adjusted = math.tanh(pnl_adjusted) # ----between 0 and 1 

        new_tendency = self.trend_strength * price_movement + pnl_adjusted + noise
        adjusted_tendency = math.tanh(new_tendency) * self.risk_tolerance

        self.tendency_val = adjusted_tendency


class ContrarianTrader(Agent):
    def __init__(self, identity, cash, holdings, risk_tolerance, PnL_memory=None, reversion_strength = 1.3, tendency_value=0):
        super().__init__(identity, cash, holdings, risk_tolerance, PnL_memory, tendency_value)
        self.type = "contrarian"
        self.reversion_strength = reversion_strength

    def compute_tendency(self, price_movement):
        noise = random.uniform(-0.2,0.2)
        new_tendency = -1 * self.reversion_strength * price_movement + 0.2 * math.tanh(self.pNl[-1]) + noise # past does always influence a lil in general. With a conntrartian agent, a lil lesser I guess
        adjusted_tendency = math.tanh(new_tendency) * self.risk_tolerance
        self.tendency_val = adjusted_tendency

    

        
