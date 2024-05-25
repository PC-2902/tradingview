"""
# https://www.mql5.com/en/docs/python_metatrader5

EurUsd -> 
10 || 6.7

Xness

Login:    124355449 
Name:     PC2902-meta5 
Password: fwaijP14# 
Server:   Exness-MT5Trial7 
Balance:  289.69


FXCM
Login    : 701825946
Password : m6iqD


"""
import MetaTrader5

class mt5():
    def mt_config(self):
        self.mt = MetaTrader5
    
    def login(self):
        self.mt.initialize()
        
        if not self.mt.initialize():
            print("initialize() failed, error code =",self.mt.last_error())
            quit()
        
        Loginn    =  124355449
        Name      =  "PC2902-meta5" 
        Password  =  "fwaijP14#"
        Server    =  "Exness-MT5Trial7"
        
        self.mt.login(Loginn, Password, Server)
    
    def acc_info(self):
        print("terminal info:",self.mt.terminal_info())
        print("account info :",self.mt.account_info())
        print("terminal info:",self.mt.terminal_info())
        print("Total Symbol",self.mt.symbols_total())

    def symbol_info_btcusd(self):
        btc_usd = self.mt.symbol_info_tick("BTCUSDm")._asdict()
        for i in btc_usd:
            print(i,":",btc_usd[i])
    
    def buy_btcusd(self):
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick("BTCUSDm").ask
        sell   = self.mt.symbol_info_tick("BTCUSDm").bid
        spread = buy - sell
        tp     = (buy + 200) + spread
        sl     = (buy - 60)  - spread
    
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.6,
        "type": self.mt.ORDER_TYPE_BUY,
        "price": buy,
        "tp": tp,
        "sl": sl,
        "type_time": self.mt.ORDER_TIME_GTC,
        "type_filling": self.mt.ORDER_FILLING_FOK,
        }
    
        self.mt.order_send(request)._asdict()
        for i in request:
            print(i,":",request[i])
    
    def sell_btcusd(self):
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick("BTCUSDm").ask
        sell   = self.mt.symbol_info_tick("BTCUSDm").bid
        spread = buy - sell
        tp     = (buy + 200) + spread
        sl     = (buy - 60)  - spread
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.6,
        "type": self.mt.ORDER_TYPE_BUY,
        "price": sell,
        "tp": tp,
        "sl": sl,
        "type_time": self.mt.ORDER_TIME_GTC,
        "type_filling": self.mt.ORDER_FILLING_FOK,
        }
    
        self.mt.order_send(request)._asdict()
        for i in request:
            print(i,":",request[i])
        
    def symbol_info_eurusd(self):
        eur_usd = self.mt.symbol_info_tick("EURUSDm")._asdict()
        for i in eur_usd:
            print(i,":",eur_usd[i])
        
    def buy_eurusd(self):
        symbol  = "EURUSDm"
        buy     = self.mt.symbol_info_tick("EURUSDm").ask
        sell    = self.mt.symbol_info_tick("BTCUSDm").bid
        spread  = buy - sell
        tp      = (buy + 33)   + spread
        sl      = (buy - 22) - spread
    
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.18,
        "type": self.mt.ORDER_TYPE_BUY,
        "price": buy,
        "tp": tp,
        "sl": sl,
        "type_time": self.mt.ORDER_TIME_GTC,
        "type_filling": self.mt.ORDER_FILLING_FOK,
        }
    
        self.mt.order_send(request)._asdict()
        for i in request:
            print(i,":",request[i])
    
    def sell_eurusd(self):
        symbol  = "EURUSDm"
        buy     = self.mt.symbol_info_tick("EURUSDm").ask
        sell    = self.mt.symbol_info_tick("BTCUSDm").bid
        spread  = buy - sell
        tp      = (buy + 33)   + spread
        sl      = (buy - 22) - spread
    
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.18,
        "type": self.mt.ORDER_TYPE_BUY,
        "price": sell,
        "tp": sl,
        "sl": tp,
        "type_time": self.mt.ORDER_TIME_GTC,
        "type_filling": self.mt.ORDER_FILLING_FOK,
        }
    
        self.mt.order_send(request)._asdict()
        for i in request:
            print(i,":",request[i])       
    

    def run_main(self):
        self.mt_config()
        self.login()
    
