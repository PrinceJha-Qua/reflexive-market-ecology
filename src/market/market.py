import random
import math
class Market:
    def __init__(self,current_price, sensitivity):
        self.current_price = current_price
        self.sensitivity = sensitivity
       
        self.price_history = [] # ----> {price,buy_pressure,sell_pressure,imbalance,returns}
       
        self.buy_pressure = 0
        self.sell_pressure = 0 
        

    def agents_act(self, action):
        for act, vol in action:
            if act == 1:
                self.buy_pressure += vol
            elif act == -1:
                self.sell_pressure += vol

    def pricing(self, tick, fear_multiplier = 1.3):
        if self.sell_pressure + self.buy_pressure == 0 :
            imbalance = 0 
        
        else : 
            imbalance = (self.buy_pressure - self.sell_pressure) / (self.buy_pressure + self.sell_pressure)  
        
        # Comment this out for experiments.....
        if imbalance < 0 and imbalance >= -0.67 :
            imbalance *= fear_multiplier # ---------> to remove demand symmetry : Fear propogates more.. then greed and optimism
             
        # to keep imbalance bounded where lets say..
        ''' there's 5 buy offer and 10 sell ----> imbalance = 5
            there's 5000 buy offer and 5005 sell ----> imbalance = 5
            but both are not same.. 
            1st is tiny market with major disagreement
            2nd is huge market with tiny disagreement '''
        
        '''
        Another silent assumption here is that somebody has to trade.. both sell and buy pressure should not become 0
        cause then imbalnce = 0/0.. so we must create an edge case for a silent market.
        '''

        returns = imbalance * self.sensitivity * math.tanh(math.log(1 + self.sell_pressure + self.buy_pressure))
        
        if (returns < 1) :
            returns = math.copysign(returns**2, returns)
        elif ( returns > 1):
            returns = 1 + returns**(1/3)
        # -----> return is the percentage change in price....
        # return = ( new_price - current_price ) / current_price
        price = max(0, returns * self.current_price + self.current_price) # Prices can go negative like the infamous oil Futures Contract's dip to negative during Covid Pandemic
        
        self.price_history.append({
            "tick": tick,
            "price": price,
            "buy_pressure": self.buy_pressure,
            "sell_pressure": self.sell_pressure,
            "total_volume": self.sell_pressure + self.buy_pressure,
            "imbalance": imbalance,
            "returns": returns
        })

        self.sell_pressure = 0
        self.buy_pressure = 0
        self.current_price = price
        return price