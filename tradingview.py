from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time
import pickle

class tradingview_main():
    
    def td_config(self):
        self.driver        = None
        self.col_btcusd    = None
        self.col_eurusd    = None
        self.col_btcusdt   = None
        self.col_bn        = None
        self.col_nifty     = None
        
    def selenium(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        option.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service('chromedriver.exe'),options=option)

    
    def loadcookie(self):
        self.driver.get("https://www.tradingview.com/accounts/signin/")
        user_name = "valoranthomeacc1@gmail.com"
        psw_name  = "AltF4Bro!!!" 

        self.driver.find_element(By.XPATH,"//span[@class='ellipsis-container-bYDQcOkp'][normalize-space()='Email']").click()
        self.driver.find_element(By.XPATH,"//input[@id='id_username']").send_keys(user_name)
        self.driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys(psw_name)
        #submit = driver.find_element(By.XPATH,"//span[contains(text(),'Sign in')]").click()

        time.sleep(20)

        cookies = self.driver.get_cookies()
        print(cookies)

        pickle.dump(cookies,open('cookies.pkl','wb')) 
    
    def usecookie(self):
        self.driver.get('https://www.tradingview.com/accounts/signin/')

        cookies = pickle.load(open("cookies.pkl", "rb"))

        for cookie in cookies:
            cookie['domain'] = ".tradingview.com"
        
            try:
                self.driver.add_cookie(cookie)
            except Exception as e:
                print(e)
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############   
   
    def chart_btcusd(self):
        time.sleep(5)
        self.driver.get("https://www.tradingview.com/chart/?symbol=FPMARKETS%3ABTCUSD")     
        print("Login Successfull")
        print("\n")
        
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
                
        # EMA-Cross
        
        signal     = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex  = Color.from_string(signal).hex
        
        print("BTCUSD =>")
        print("Efmus    :",ef1hex)
        print("EMA-Cross:",signalhex) 
        self.col_btcusd    = [ef1hex, signalhex]
    
    def color_ident_btc(self):
        b = self.col_btcusd
        if all(color == "#00ff00" for color in b):
            #print("BTC Green")
            unit = "BTC Green"
        elif all(color == "#ff0000" for color in b):
            #print("BTC Red")
            unit = "BTC Red"
        else:
            #print("BTC Avoid")
            unit = "avoid"
        return unit
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    def chart_btcusdt(self):
        time.sleep(5)
        self.driver.get("https://in.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT")     
        print("\n")
        # EFmus
        time.sleep(5)    
   
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
                
        # EMA-Cross
        
        signal     = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex  = Color.from_string(signal).hex
        
        print("BTCUSDT =>")
        print("Efmus    :",ef1hex)
        print("EMA-Cross:",signalhex) 
        self.col_btcusdt    = [ef1hex, signalhex]
    
    def color_ident_btcusdt(self):
        b = self.col_btcusdt
        if all(color == "#00ff00" for color in b):
            #print("BTC Green")
            unit = "BTCusdt Green"
        elif all(color == "#ff0000" for color in b):
            #print("BTC Red")
            unit = "BTCusdt Red"
        else:
            #print("BTC Avoid")
            unit = "avoid"
        return unit

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def chart_eurusd(self):
        time.sleep(5)
        self.driver.get("https://www.tradingview.com/chart/?symbol=FPMARKETS%3AEURUSD")     
        print("\n")
        
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
        
        # EMA-Cross
        
        signal     = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex  = Color.from_string(signal).hex
        
        print("EurUsd =>")
        print("Efmus    :",ef1hex)
        print("EMA-Cross:",signalhex) 
        self.col_eurusd    = [ef1hex, signalhex]
    
    def color_ident_eurusd(self):
        b = self.col_eurusd
        if all(color == "#00ff00" for color in b):
            #print("BTC Green")
            unit = "EurUsd Green"
        elif all(color == "#ff0000" for color in b):
            #print("BTC Red")
            unit = "EurUsd Red"
        else:
            #print("BTC Avoid")
            unit = "avoid"
        return unit
    
    ###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def chart_gold(self):
        time.sleep(5)
        self.driver.get("https://www.tradingview.com/chart/?symbol=FPMARKETS%3AXAUUSD")     
        print("\n")
        
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
                
        # EMA-Cross
        
        signal     = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex  = Color.from_string(signal).hex
        
        print("Gold =>")
        print("Efmus    :",ef1hex)
        print("EMA-Cross:",signalhex) 
        self.col_gold    = [ef1hex, signalhex]
    
    def color_ident_gold(self):
        b = self.col_gold
        if all(color == "#00ff00" for color in b):
            #print("BTC Green")
            unit = "Gold Green"
        elif all(color == "#ff0000" for color in b):
            #print("BTC Red")
            unit = "Gold Red"
        else:
            #print("BTC Avoid")
            unit = "avoid"
        return unit

    def run_uscap(self):
        
        try:
            self.selenium()
            self.usecookie()
        
            self.chart_btcusd()
            self.chart_btcusdt()
            self.chart_eurusd()
            self.chart_gold()
            self.driver.quit()
        
            a = self.color_ident_btc()
            b = self.color_ident_btcusdt()
            c = self.color_ident_eurusd()
            d = self.color_ident_gold()

            print("\n")
            uscap = [a, b, c, d]
            return uscap
        except Exception as e:
            print("Check Internet\nTradingView Scrapping Eroor")
            print(e)
        
        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    

    def chart_banknifty(self):
        time.sleep(5)
        self.driver.get("https://in.tradingview.com/chart/?symbol=NSE%3ABANKNIFTY")        
        print("\nLogin Successfull")     
        print("\n")
        
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
                
        # EMA-Cross
        
        signal     = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex  = Color.from_string(signal).hex
        
        print("BankNifty =>")
        print("Efmus    :",ef1hex)
        print("EMA-Cross:",signalhex) 
        self.col_banknifty    = [ef1hex, signalhex]
    
    def color_ident_banknifty(self):
        b = self.col_banknifty
        if all(color == "#00ff00" for color in b):
            #print("BTC Green")
            unit = "BankNifty Green"
        elif all(color == "#ff0000" for color in b):
            #print("BTC Red")
            unit = "BankNifty Red"
        else:
            #print("BTC Avoid")
            unit = "avoid"
        return unit
    
    ###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
    def chart_nifty(self):
        time.sleep(5)
        self.driver.get("https://in.tradingview.com/chart/?symbol=NIFTY")     
        print("\n")
        
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
                
        # EMA-Cross
        
        signal     = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex  = Color.from_string(signal).hex
        
        print("Nifty =>")
        print("Efmus    :",ef1hex)
        print("EMA-Cross:",signalhex) 
        self.col_nifty    = [ef1hex, signalhex]
    
    def color_ident_nifty(self):
        b = self.col_nifty
        if all(color == "#00ff00" for color in b):
            #print("BTC Green")
            unit = "Nifty Green"
        elif all(color == "#ff0000" for color in b):
            #print("BTC Red")
            unit = "Nifty Red"
        else:
            #print("BTC Avoid")
            unit = "avoid"
        return unit
    
    ###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
    def chart_finnifty(self):
        time.sleep(5)
        self.driver.get("https://in.tradingview.com/chart/?symbol=NSE%3ACNXFINANCE")     
        print("\n")
        
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
                
        # EMA-Cross
        
        signal     = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex  = Color.from_string(signal).hex
        
        print("Fin Nifty =>")
        print("Efmus    :",ef1hex)
        print("EMA-Cross:",signalhex) 
        self.col_nifty    = [ef1hex, signalhex]
    
    def color_ident_finnifty(self):
        b = self.col_nifty
        if all(color == "#00ff00" for color in b):
            #print("BTC Green")
            unit = "FinNifty Green"
        elif all(color == "#ff0000" for color in b):
            #print("BTC Red")
            unit = "FinNifty Red"
        else:
            #print("BTC Avoid")
            unit = "avoid"
        return unit
    
    ###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
    def chart_Nniftymidcap(self):
        time.sleep(5)
        self.driver.get("https://in.tradingview.com/chart/?symbol=NSE%3ANIFTY_MID_SELECT")     
        print("\n")
        
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
                
        # EMA-Cross
        
        signal     = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex  = Color.from_string(signal).hex
        
        print("Nifty Mid Cap =>")
        print("Efmus    :",ef1hex)
        print("EMA-Cross:",signalhex) 
        self.col_nifty    = [ef1hex, signalhex]
    
    def color_ident_niftymidcap(self):
        b = self.col_nifty
        if all(color == "#00ff00" for color in b):
            #print("BTC Green")
            unit = "NiftyMidCap Green"
        elif all(color == "#ff0000" for color in b):
            #print("BTC Red")
            unit = "NiftyMidCap Red"
        else:
            #print("BTC Avoid")
            unit = "avoid"
        return unit

    def run_indcap(self):
        
        try:            
            self.selenium()
            self.usecookie()
        
            self.chart_banknifty()
            self.chart_nifty()
            self.chart_finnifty()
            self.chart_Nniftymidcap()
            self.driver.quit()
        
            a = self.color_ident_banknifty()
            b = self.color_ident_nifty()
            c = self.color_ident_finnifty()
            d = self.color_ident_niftymidcap()
        
            print("\n")
            indcap = [a, b, c, d]
            return indcap
        except Exception as e:
            print("Check Internet\nTradingView Scrapping Eroor")
            print(e)
            

        

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
    



#t = tradingview_main()
#z = t.run_indcap()
#z = t.run_uscap() 
#print(z)


    
    

"""


## Trail ##

## IDN CAP ##

9:15
sleep(2*60)
9:17
while True:

=>  9:17
    run()
    9:17:32 => sleep(28)
    9:18
    
    sleep(3480)
    10:17  <=

## USA CAP ##

9:30
sleep(2*60)
9:32
while True:

=>  9:32
    run()
    9:32:42 => sleep(18)
    9:33
    
    sleep(3480)
    10:32  <=



## IND && USA CAP ##

9:15
sleep(2*60)
9:17

while True:

=>  9:17
    run_ind()
    9:17:32 => sleep(28)
    9:18
    
    sleep(12*60 + 2*60) 9:30 => 9:32
    9:32
    run()
    9:32:42 => sleep(18)
    9:33
    
    sleep(3590) <=
    10:17
    
    
    
    

"""


