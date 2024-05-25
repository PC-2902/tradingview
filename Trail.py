"""

def td():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

class main():
    def __init__(self):
        self.driver = None

    
    
    def color_ele():
        search = driver.get("https://www.prestigeconstructions.com/")
        time.sleep(5)
        ele = driver.find_element(By.ID,"btn-resprojects").value_of_css_property("background-color")
        print(ele)
        elehex = Color.from_string(ele).hex
        print(elehex)


    def tradingview():
        user_name = "valoranthomeacc1@gmail.com" 
        psw = "AltF4Bro!!!"
        search = driver.get("https://www.tradingview.com/accounts/signin/")
        login_email = driver.find_element(By.XPATH,"//span[@class='ellipsis-container-bYDQcOkp']").click()
        login_user = driver.find_element(By.XPATH,"//input[@id='id_username']").send_keys(user_name)
        login_psw = driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys(psw)
        submit = driver.find_element(By.XPATH,"//span[contains(text(),'Sign in')]").click()
        print("Login Sucess")
    
        time.sleep(25)
        print("BN")
    
        ## BN search 
    
        bn = driver.get("https://in.tradingview.com/chart/ihurYfIS/?symbol=NSE%3ABANKNIFTY")
        time.sleep(10)
    
        #TrendMeter
        bn_ele = driver.find_element(By.XPATH,"//div[contains(text(),'20.00')]").value_of_css_property("color")
        bn_col = Color.from_string(bn_ele).hex
        print("Trend-Meter",bn_col)
    
        #efmus
        #1 
        bn_ele1 = driver.find_element(By.XPATH,"//div[contains(text(),'0.20')]").value_of_css_property("color")
        bn_col2 = Color.from_string(bn_ele1).hex
        #print("Efmus 1:",bn_col2)
        #2
        bn_ele3 = driver.find_element(By.XPATH,"//div[contains(text(),'0.10')]").value_of_css_property("color")
        bn_col3 = Color.from_string(bn_ele3).hex
        #print("Efmus 2:",bn_col3)#
        bn_ele4 = driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        bn_col4 = Color.from_string(bn_ele4).hex 
        print(bn_col2,":",bn_col3,":",bn_col4)
    

## fun

z = ["green", "red", "avoid"]

def color():
    return "\n".join(z)

c = color()
print(c)

## range 


def array1():
    
    a = ["hi","bye"]
    
    for i in range(0, len(a)):
        print(a[i])
        


def color_ident2():
    green = "#00ff00"
    red   = "#ff0000"
    
    a = ["#00ff00", "#00ff00", "#00ff00", "#00ff00", "#ff0000"]
    
    for i in range(0,len(a)):
        if a[i] == green or a[i] == red:
            print("All same")
            break
    else:
        print("Avoid")
    


1 hr   -> 3600 s   
15 min -> 900  s 
5 mins -> 300  s 

***********************
# 1st run
run() 
sleep(120)  ->5
run() 
sleep(120)  ->5
run() 
sleep(60)   ->1
        
# 2nd Run
sleep(4500) ->10
run()
sleep(120)
run
sleep(120)
run
sleep(60)
run()

#3rd
        
*********************


    

#print(time.ctime(time.time()))



class computer:
    
    def config(self):
        print("I5 \n16Gb ram \n1TB storage")
        x = 10
        return x
        

obj = computer()
c = obj.config()

print(c)



import telegram

obj = telegram.sample()

obj = obj.trial()

print(obj)

def color_idnt1():
        b = ["#00ff00" ,"#00ff00", "#00ff00", "#ff0000"]
        green = "#00ff00"
        red   = "#ff0000"
        co = None
        flag = False 
        
        for i in range(0,len(b)):
            if b[i] == green and (co == None or co == green):
                co = green
                continue
            elif b[i] == green and co == red:
                print("They are different")
                flag = True
                unit = "AVOID"
                break
            
            elif b[i] == red and (co == None or co == red):
                co = red
                continue
            elif b[i] == red and co == green:
                print("They are different")
                unit = "AVOID"
                flag = True
                 
        if not flag:
                if co == green:
                    print("All Green")
                    unit = "Operation-> All GREEN"
                                  
                else:
                    print("All Red")
                    unit = "Operation-> All RED"
        return unit
         
obj = color_idnt1()
print(obj)

import telebot 
import tradingview

tr = tradingview.tradingview_main()
bot = telebot.TeleBot('6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI')

@bot.message_handler(commands=['run'])
def echo_message(message):
    
        tr.run()
        print("1")
        bot.send_message(message.chat.id, tr.color_idnt())
        while True:
            tr.run_loop()
            bot.send_message(message.chat.id, tr.color_idnt())
            print("2")

bot.polling()


import telebot

# Create a new TeleBot instance
bot = telebot.TeleBot('YOUR_API_TOKEN')

# Handle the /start command
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello! I am your Telegram bot.')

# Handle the /echo command
@bot.message_handler(commands=['echo'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

# Start the bot
bot.polling()


#OpenAI API KeY : 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

import schedule
import time

class Main:
    def __init__(self):
        self.schedule = schedule
    
    def bedtime(self):
        print("Hello World")

    def time(self):
        self.schedule.every().day.at("23:13").do(self.bedtime)
        
        # Loop to run the schedule
        while True:
            self.schedule.run_pending()
import tradingview

tr = tradingview.tradingview_main()

def echo_message(message):
        tr.run()
        bot.send_message(message.chat.id, tr.color_idnt()) 
        time.sleep(3)
        tr.run()
        bot.send_message(message.chat.id, tr.color_idnt()) 
        print("\n\n Main Program Completed \n\n")
        
        while True:
            time.sleep(180) 
            print(time.ctime(time.time()),"\n\n 3 mins completed \n")
            tr.run_loop   
            bot.send_message(message.chat.id, tr.color_idnt())         
            
            time.sleep(3420) # 1hr |=> 3600 - 180 
            print(time.ctime(time.time()),"\n\n 1 Hr completed \n\n")
            tr.run_loop() 
            bot.send_message(message.chat.id, tr.color_idnt())
            print("\n\n     \n\n")
        
     
 
###########################################################################################################################################################################################
#Cookies

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)


class loadcookies():
    def __init__(self):
        c = None
    
    def logintd(self):
        driver.get("https://www.tradingview.com/accounts/signin/")
        user_name = "valoranthomeacc1@gmail.com"
        psw_name  = "AltF4Bro!!!" 

        email = driver.find_element(By.XPATH,"//span[@class='ellipsis-container-bYDQcOkp'][normalize-space()='Email']").click()
        user = driver.find_element(By.XPATH,"//input[@id='id_username']").send_keys(user_name)
        psw = driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys(psw_name)
        #submit = driver.find_element(By.XPATH,"//span[contains(text(),'Sign in')]").click()

        time.sleep(20)

        cookies = driver.get_cookies()
        print(cookies)

        pickle.dump(cookies,open('cookies.pkl','wb'))  
        

class usecookie():
    def __init__(self):
        c = None
    
    driver.get('https://www.tradingview.com/accounts/signin/')

    cookies = pickle.load(open("cookies.pkl", "rb"))

    for cookie in cookies:
        cookie['domain'] = ".tradingview.com"
        
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(e)

    driver.get('https://in.tradingview.com/chart')

    time.sleep(10)


class tradingview_main():
    
    def __init__(self):
        self.driver = None
        self.col    = None
        
    def selenium(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    
    def loadcookie(self):
        self.driver.get("https://www.tradingview.com/accounts/signin/")
        user_name = "valoranthomeacc1@gmail.com"
        psw_name  = "AltF4Bro!!!" 

        email = self.driver.find_element(By.XPATH,"//span[@class='ellipsis-container-bYDQcOkp'][normalize-space()='Email']").click()
        user  =  self.driver.find_element(By.XPATH,"//input[@id='id_username']").send_keys(user_name)
        psw   =   self.driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys(psw_name)
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

        self.driver.get('https://in.tradingview.com/chart')





class search():
    def __init__(self):
        self.driver = None
    
    def seleium(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    
    def yt1(self):
        google = self.driver.get("https://www.youtube.com/")
        time.sleep(3)
        eleytcolor = self.driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("Hello")
        click      = self.driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys(Keys.ENTER)
        
    
    def yt2(self):
        self.driver.switch_to.new_window()
        time.sleep(3)
        yt = self.driver.get("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
        click = self.driver.find_element(By.XPATH,"//div[normalize-space()='Gaming']").click()
        ele = self.driver.find_element(By.XPATH,"//div[normalize-space()='Gaming']").value_of_css_property('color')
        ele = Color.from_string(ele).hex
        print(ele)
        
    
    
    def run(self):
        self.seleium()
        self.yt1()
        self.yt2()
    


a = search()
a.run()


formula : 
    # initial run()
    
    # get color 
    a = color
    print(a)    [optional]
    
    #sleep(180) 3 mins
    
    # while True
        run_loop()
        
        # get color
        b = color
        
        # check 
        if a != b:
            bot.send()
        else:
            pass



class telemain():
    def __init__(self):
        self.bot = None
        self.tr  = None
    
    def tradingconfig(self):
        self.tr = tradingview.tradingview_main()
        self.bot = telebot.TeleBot('6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI')

    def start(self):
        @self.bot.message_handler(commands=['run'])
        def echo_message(message):
            self.tr.run()
            self.bot.send_message(message.chat.id, self.tr.color_idnt())            # 20 sec || 33 sec
            col1 = self.tr.color_idnt()
            print("\n\n Main Program Completed \n\n")
            time.sleep(230)                                                         # PC 230 || LAPTOP 238 
        
            while True:
                time.sleep(3600)                                                      # 1hr |=> 3600 
                print("\n\n 1 Hr completed \n\n",time.ctime(time.time()))
                self.tr.run_loop() 
                
                col2 = self.tr.color_idnt()
                print(col2)

                if col1 != col2:
                    self.bot.send_message(message.chat.id, self.tr.color_idnt())
                    
                else:
                    pass
                
    def run(self):
        self.tradingconfig()
        self.start()

a = telemain()
a.run()
a.bot.polling()




import telebot
import tradingview
import time
import schedule


class telemain():
    def __init__(self):
        self.bot      = None
    
    def tradingconfig(self):
        self.bot = telebot.TeleBot('YOUR_TOKEN')

    def start(self):
        @self.bot.message_handler(commands=['run'])
        def echo_message(message):
            self.bot.send_message(message.chat.id, "Hello")                    
                
    def start1(self):
        @self.bot.message_handler(commands=['run1'])
        def echo_message(message):
            self.bot.send_message(message.chat.id, "Hello")                    
    
    
    def run(self):
        self.tradingconfig()
        self.start()
        
 
    def timeshedule(self):
    
        self.schedule.every().day.at("17:32").do(self.run)
        
        while True:
            self.schedule.run_pending()
            
    
a = telemain()
a.run()
#a.timeshedule()
a.bot.polling()



def echo_message(message,self):
            
            self.tr.run()
            a = self.tr.color_idnt() #g
            
            if a == "AVOID":
                print("skip")
            else:
                self.bot.send_message(message.chat.id, self.tr.color_idnt())       # 20 sec || 33 sec
            
            print("\n\n Main Program Completed \n\n")
            time.sleep(230)                                                        # PC 230 || LAPTOP 238 
            
            b = None
            c = None
                       
            while True:
                time.sleep(3600)                                                   # 1hr |=> 3600 
                self.tr.run_loop()
                b = self.tr.color_idnt()
                
                if b == "AVOID":
                    print("skip")
                
                elif b == a:
                    print("Skip")
                
                elif b == c:
                    print("Skip")
                
                else:
                    self.bot.send_message(message.chat.id, self.tr.color_idnt()) 
                    
                
                time.sleep(3600)                                                   # 1hr |=> 3600 
                self.tr.run_loop()
                c = self.tr.color_idnt()
                
                if c == "AVOID":
                    print("skip")
                
                elif c == b:
                    print("Skip")
                
                else:
                    self.bot.send_message(message.chat.id, self.tr.color_idnt())
                
                a = "AVOID"
     



from selenium.common.exceptions import NoSuchElementException

try:
    elem = driver.find_element_by_xpath(".//*[@id='SORM_TB_ACTION0']")
    elem.click()
except NoSuchElementException:  #spelling error making this code not work as expected
    pass



    
import telebot
import tradingview
import time
from selenium.common.exceptions import NoSuchElementException

class telemain():
    def __init__(self):
        self.bot      = None
        self.tr       = None
    
    def tradingconfig(self):
        self.tr = tradingview.tradingview_main()
        self.bot = telebot.TeleBot('6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI')

    
    def start(self):
        @self.bot.message_handler(commands=['run'])
        def echo_message(message):
           
            self.tr.run()
            a = self.tr.color_idnt() 
            
            if a == "AVOID":
                print("skip")
            else:
                #self.bot.send_message(message.chat.id, self.tr.color_idnt())       # 20 sec || 33 sec
                print(a)
        
            print("\n\n Main Program Completed \n\n")
            #time.sleep(230)                                                       # PC 230 || LAPTOP 238
            time.sleep(60)                                               
            
            b = None
            c = None
                       
            while True:
                #time.sleep(3600)                                                   # 1hr |=> 3600 
                print(time.ctime(time.time()))
                self.tr.run_loop()
                b = self.tr.color_idnt()
                
                if b == "AVOID":
                    print("skip")
                
                elif b == a:
                    print("Skip")
                
                elif b == c:
                    print("Skip")
                
                else:
                    #self.bot.send_message(message.chat.id, self.tr.color_idnt()) 
                    print(b)
                
                time.sleep(60)                                                   # 1hr |=> 3600 
                print(time.ctime(time.time())) 
                self.tr.run_loop()
                c = self.tr.color_idnt()
                
                if c == "AVOID":
                    print("skip")
                
                elif c == b:
                    print("Skip")
                
                else:
                    #self.bot.send_message(message.chat.id, self.tr.color_idnt())
                    print(c)
                a = "AVOID"
            
                time.sleep(60)
                #
    
    def run(self):
        self.tradingconfig()
        self.start()
        
   

   
a = telemain()
a.run()
a.bot.polling() 

import MetaTrader5 as mt5

Login    =  124355449
Name     =  "PC2902-meta5" 
Password =  "fwaijP14#"
Server   =  "Exness-MT5Trial7" 



 
mt5.initialize()

a = mt5.login(Login,Password,Server)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

def mt_info():
    #print("terminal info:",mt5.terminal_info())
    print("account info :",mt5.account_info())
    #print("terminal info:",mt5.terminal_info())
    #print("Total Symbol",mt5.symbols_total())

def symbol_info():
    btc_usd = mt5.symbol_info_tick("BTCUSDm")._asdict()
    for i in btc_usd:
        #print("  {}={}".format(prop, btc_usd[prop]))
        print(i,":",btc_usd[i])


def order_buy():
    symbol = "BTCUSDm"
    buy    = mt5.symbol_info_tick("BTCUSDm").ask
    #sell   = mt5.symbol_info_tick("BTCUSDm").bid
    tp     = buy + 100
    sl     = buy - 66
    
    request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": 0.6,
    "type": mt5.ORDER_TYPE_BUY,
    "price": buy,
    "tp": buy + 100,
    "sl": buy - 66,
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_FOK,
    }
    
    orders = mt5.order_send(request)._asdict()
    for i in request:
        print(i,":",request[i])


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
import time 
import pickle
import threading

class tradingview_main():
    
    def td_config(self):
        self.driver        = None
        self.col_btcusd    = None
        self.col_bn        = None
        self.col_eurusd    = None
        
    def selenium(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    
    def loadcookie(self):
        self.driver.get("https://www.tradingview.com/accounts/signin/")
        user_name = "valoranthomeacc1@gmail.com"
        psw_name  = "AltF4Bro!!!" 

        email = self.driver.find_element(By.XPATH,"//span[@class='ellipsis-container-bYDQcOkp'][normalize-space()='Email']").click()
        user  =  self.driver.find_element(By.XPATH,"//input[@id='id_username']").send_keys(user_name)
        psw   =   self.driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys(psw_name)
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
       
    
    def chart_btcusd(self):
        self.driver.get("https://in.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT")
        print(time.ctime(time.time()))
        print("Login Successfull")

        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
        
        ef2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        ef2hex = Color.from_string(ef2).hex
        
        

       #Trend-Meter 
        time.sleep(5)
        tm1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")                                                
        tm1hex = Color.from_string(tm1).hex

        tm2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        tm2hex = Color.from_string(tm2).hex
        
        tm3    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        tm3hex = Color.from_string(tm3).hex
        
        print("BTCUSD:")
        print("Efmus:       ",ef1hex , ef2hex,       )
        print("Trend-Meter: ",tm1hex, tm2hex, tm3hex)
        
        self.col_btcusd = [ef1hex , ef2hex , tm1hex , tm2hex, tm3hex]
        
        
        ## Color Identi block
        
        b = self.col_btcusd
        green = "#00ff00"
        red   = "#ff0000"
        co = None
        flag = False 
                
        for i in range(0,len(b)):
            if b[i] == green and (co == None or co == green):
                co = green
                continue
            elif b[i] == green and co == red:
                #print("They are different")
                flag = True
                unit = "AVOID"
                break
            
            elif b[i] == red and (co == None or co == red):
                co = red
                continue
            elif b[i] == red and co == green:
                #print("They are different")
                unit = "AVOID"
                flag = True
                 
        if not flag:
                if co == green:
                    print("BTCUSD: All Green")
                    unit = "BTCUSD: All GREEN"
                                  
                else:
                    print("BTCUSD: All Red")
                    unit = "BTCUSD: All RED"
        return unit
    
    def chart_bn(self):
        self.driver.switch_to.new_window()
        self.driver.get("https://in.tradingview.com/chart/?symbol=NSE%3ABANKNIFTY")      
 
       
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
        
        ef2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        ef2hex = Color.from_string(ef2).hex
        
       
        
        #Trend-Meter 
        time.sleep(5)
        tm1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")                                                
        tm1hex = Color.from_string(tm1).hex

        tm2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        tm2hex = Color.from_string(tm2).hex
        
        tm3    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        tm3hex = Color.from_string(tm3).hex
        
        print("\nBankNifty") 
        print("Efmus:       ", ef1hex, ef2hex,       )
        print("Trend-Meter: ", tm1hex, tm2hex, tm3hex)
        
        self.col_bn = [ef1hex , ef2hex , tm1hex , tm2hex, tm3hex]

        ## Color Identi block
        
        b = self.col_bn
        green = "#00ff00"
        red   = "#ff0000"
        co = None
        flag = False 
                
        for i in range(0,len(b)):
            if b[i] == green and (co == None or co == green):
                co = green
                continue
            elif b[i] == green and co == red:
                #print("They are different")
                flag = True
                unit = "AVOID"
                break
            
            elif b[i] == red and (co == None or co == red):
                co = red
                continue
            elif b[i] == red and co == green:
                #print("They are different")
                unit = "AVOID"
                flag = True
                 
        if not flag:
                if co == green:
                    print("BankNifty: All Green")
                    unit = "bankNifty: All GREEN"
                                  
                else:
                    print("BankNifty: All Red")
                    unit = "Banknifty: All RED"
        #print("\n",time.ctime(time.time()))                    
        return unit
        
    def chart_eurusd(self):
        self.driver.switch_to.new_window()
        self.driver.get("https://in.tradingview.com/chart/?symbol=EASYMARKETS%3AEURUSD")      
 
       
        # EFmus
        time.sleep(5)    
        ef1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        ef1hex = Color.from_string(ef1).hex
        
        ef2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        ef2hex = Color.from_string(ef2).hex
        
       
        
        #Trend-Meter 
        time.sleep(5)
        tm1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")                                                
        tm1hex = Color.from_string(tm1).hex

        tm2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        tm2hex = Color.from_string(tm2).hex
        
        tm3    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        tm3hex = Color.from_string(tm3).hex
        
        print("\nEURUSD") 
        print("Efmus:       ", ef1hex, ef2hex,       )
        print("Trend-Meter: ", tm1hex, tm2hex, tm3hex)
        
        self.col_eurusd = [ef1hex , ef2hex , tm1hex , tm2hex, tm3hex]
        
        ## Color Identi block
        
        b = self.col_eurusd
        green = "#00ff00"
        red   = "#ff0000"
        co = None
        flag = False 
                
        for i in range(0,len(b)):
            if b[i] == green and (co == None or co == green):
                co = green
                continue
            elif b[i] == green and co == red:
                #print("They are different")
                flag = True
                unit = "AVOID"
                break
            
            elif b[i] == red and (co == None or co == red):
                co = red
                continue
            elif b[i] == red and co == green:
                #print("They are different")
                unit = "AVOID"
                flag = True
                 
        if not flag:
                if co == green:
                    print("EURUSD: All Green")
                    unit = "EURUSD: All GREEN"
                                  
                else:
                    print("EURUSD: All Red")
                    unit = "EURUSD: All RED"
        #print("\n",time.ctime(time.time()))                    
        
        return unit      
    
    def reload_cookie(self):
        self.selenium()
        self.loadcookie()
        
    
    def run_btc(self):
        
        self.selenium()
        self.usecookie()
        self.chart_btcusd()
    
    def run_bn(self):
        self.chart_bn()
    
    def run_eur(self):
        self.chart_eurusd()
        
    
    def run_main(self):
        self.run_btc()
        self.run_bn()
        self.run_eur()

        self.driver.quit()
     
    def run_loop(self):
        time.sleep(60)
        while True:
            time.sleep(120)
            self.run_btc()
            self.run_bn()
            self.run_eur()
            
            self.driver.quit()

a = tradingview_main()
a.run_main()
a.run_loop()
        

############ 

btc = tr.color_ident_bt()
bn  = tr.color_ident_bn()
eur = tr.color_ident_eur()

variables = {"btc": btc, "bn": bn, "eur": eur}

for var_name, var_value in variables.items():
    if var_value != "AVOID" and var_value in ["AVOID", "btc all green", "btc all red", "bn all green","bn all red","eur all green","eur all red"]:
            print(var_value)


import telebot
import tradingview
import time

class telemain():
        
    def tradingconfig(self):
        self.tr = tradingview.tradingview_main()
        self.bot = telebot.TeleBot('6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI')

    
    def start(self):
        @self.bot.message_handler(commands=['run'])
        def echo_message(message):
           
            self.bot.send_message(message.chat.id,"Bot has started")
            self.tr.run_main()
            
            # A
            btc = self.tr.color_ident_bt()
            bn  = self.tr.color_ident_bn()
            eur = self.tr.color_ident_eur()

            variables = {"btc": btc, "bn": bn, "eur": eur}

            for i in variables:
                if variables[i] != "AVOID":
                    print(variables[i])
                    self.bot.send_message(message.chat.id,variables[i])
            
            time.sleep(171) # 3.5 mins
            while True:
                
                # B
                
                time.sleep(3600) # 1 hr
                self.tr.run_main()
                
                btc1 = self.tr.color_ident_bt()
                bn1  = self.tr.color_ident_bn()
                eur1 = self.tr.color_ident_eur()
                
                variables = {"btc1": btc1, "bn1": bn1, "eur1": eur1}
                
                for j in variables:
                    if variables[j] == "AVOID":
                        print("")
                    
                    elif variables[j] == variables[i]:
                        print("")
                    
                    elif variables[k] == variables[j]:
                        print("")
                    
                    else:
                        print(variables[j])
                        self.bot.send_message(message.chat.id,variables[j])

                # C 
                
                time.sleep(3600)
                self.tr.run_main()
                
                btc3 = self.tr.color_ident_bt()
                bn3  = self.tr.color_ident_bn()
                eur3 = self.tr.color_ident_eur()
                
                variables = {"btc3": btc3, "bn3": bn3, "eur3": eur3}
                
                for k in variables:
                    if variables[k] == "AVOID":
                        print("")
                    
                    elif variables[k] == variables[j]:
                        print("")
                    
                    else:
                        print(variables[j])
                        self.bot.send_message(message.chat.id,variables[j])
                
                variables[i] = None

a = telemain()
a.tradingconfig()
a.start()
a.bot.polling()
            

        
btc = "btc green"            
bn  = "bn green"
eur = "avoid"

btc1 = "btc green"            
bn1  = "bn green"
eur1 = "avoid"

btc2 = "btc green"            
bn2  = "avoid"
eur2 = "eur red"



variables = [btc, bn, eur]
variables1 = [btc1, bn1, eur1]
variables2 = [btc2, bn2, eur2]


def temp():
    for i in variables:
        #print(i)
        if i != "avoid":
            print(i)
        else:
            pass
            

def trail_loop():
    # Convert lists to sets for efficient comparison
    set_variables = set(variables)
    set_variables1 = set(variables1)

    # Find unique elements in variables1 that don't repeat in variables
    unique_elements = set_variables1 - set_variables

    # Convert the set to a string and print
    unique_elements_string = '\n'.join(unique_elements)
    print(unique_elements_string)

    ###
    set_variables1 = set(variables1)
    set_variables2 = set(variables2)
    
    unique_elements1 = set_variables2 - set_variables1

    
    unique_elements_string1 = '\n'.join(unique_elements1)
    print(unique_elements_string1)
    
trail_loop()    



btc = "btc green"            
bn  = "avoid"
eur = "eur green"

btc1 = "btc green"            
bn1  = "bn red"
eur1 = "avoid"

btc2 = "btc red"            
bn2  = "bn red"
eur2 = "eur red"



variables = [btc, bn, eur]
variables1 = [btc1, bn1, eur1]
variables2 = [btc2, bn2, eur2]



result_two_three_output = None

def temp2():
    
    # A
    
    variables = [btc, bn, eur]
    for i in variables:
        #print(i)
        if i != "avoid":
            print(i)
            # bot.send()
        else:
            pass
    
    while True:
        # B 
        variables1 = [btc1, bn1, eur1]
        one = set(variables)
        two = set(variables1)
    
        result_one_two = two - one
    
        result_one_two_output = "\n".join(result_one_two)
        #print(result_one_two_output)
        if result_one_two_output != result_two_three_output:
            print(result_one_two_output)
    
        # C
        print("\nC\n")

        variables2 = [btc2, bn2, eur2]
        two = set(variables1)
        three = set(variables2)
    
        result_two_three = three - two
    
        result_two_three_output = "\n".join(result_two_three)
        print(result_two_three_output)



import telebot
import tradingview
import time
import requests

class telemain():
        
    def tradingconfig(self):
        self.tr = tradingview.tradingview_main()
        self.bot = telebot.TeleBot('6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI')

    
    def start(self):
        @self.bot.message_handler(commands=['run'])
        def echo_message(message):
           
            self.bot.send_message(message.chat.id,"Bot has started")
            self.tr.run_main()
            
            # A
            btc = self.tr.color_ident_bt()
            bn  = self.tr.color_ident_bn()
            eur = self.tr.color_ident_eur()
            variables = [btc, bn, eur]

            for i in variables:
                #print(i)
                if i != "avoid":
                    print(i)
                    #self.bot.send_message(message.chat.id,i)
                    
            time.sleep(171) # 3.5 mins
            result_two_three_output = None
            while True:
                # B
                
                time.sleep(3600) # 1 hr
                self.tr.run_main()
                
                btc1 = self.tr.color_ident_bt()
                bn1  = self.tr.color_ident_bn()
                eur1 = self.tr.color_ident_eur()
                variables1 = [btc1, bn1, eur1]
                
                one = set(variables)
                two = set(variables1)
    
                result_one_two = two - one
    
                result_one_two_output = "\n".join(result_one_two)
                #print(result_one_two_output)
                if result_one_two_output != result_two_three_output:
                    print(result_one_two_output)
                    #self.bot.send_message(message.chat.id,result_one_two_output)

                # C
                
                btc2 = self.tr.color_ident_bt()
                bn2  = self.tr.color_ident_bn()
                eur2 = self.tr.color_ident_eur()
                variables2 = [btc2, bn2, eur2]
                
                two = set(variables1)
                three = set(variables2)

                result_two_three = three - two
    
                result_two_three_output = "\n".join(result_two_three)
                print(result_two_three_output)
                #self.bot.send_message(message.chat.id,result_two_three_output)

                one = None

import telebot
import tradingview
import time
import requests

class telemain():
        
    def tradingconfig(self):
        self.tr = tradingview.tradingview_main()
        self.bot = telebot.TeleBot('6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI')

    
    def start(self):
        @self.bot.message_handler(commands=['run'])
        def echo_message(message):
           
            self.bot.send_message(message.chat.id,"Bot has started")
            self.tr.run_main()
            
            # A
            btc = self.tr.color_ident_bt()
            bn  = self.tr.color_ident_bn()
            eur = self.tr.color_ident_eur()

            url = "https://differentiator-microservice.vercel.app/api/diff"

            data = {
                "btc": btc,
                "bn": bn,
                "eur": eur
            }

            response = requests.post(url, data=data)

            print(response.json())
            #self.bot.send_message(message.chat.id,)
            
            #time.sleep(171) # 3.5 mins
            time.sleep(60) # 1 min
            while True:
                
                # B
                
                #time.sleep(3600) # 1 hr
                time.sleep(60) # 
                self.tr.run_main()
                
                btc1 = self.tr.color_ident_bt()
                bn1  = self.tr.color_ident_bn()
                eur1 = self.tr.color_ident_eur()
                
                time.sleep(60) # 
        

#A
a = ["btc green", "AVOID", "AVOID"]

#B
a = ["btc green", "AVOID", "AVOID"]
b = ["btc red", "AVOID", "eur red"]

for item_b in b:
    found_match = False
    for item_a in a:
        if item_b == item_a:
            found_match = True
            break
    if not found_match:
        if item_b != "AVOID":
            #print(item_b)
            print

#C
b = ["AVOID", "bn red", "eur red"]
c = ["btc red", "AVOID", "eur green"]

for item_c in c:
    found_match = False
    for item_b in b:
        if item_c == item_b:
            found_match = True
            break
    if not found_match:
        if item_c != "AVOID":
            print(item_c)
           
a = None

#D || #B

a = ["btc green", "AVOID", "AVOID"]
c = None
b = ["btc red", "AVOID", "eur red"]

for item_b in b:
    if item_b != "AVOID":
        match_a = False
        match_c = False
        
        if a is not None:
            for item_a in a:
                if item_b == item_a:
                    match_a = True
                    break
        
        if c is not None:
            for item_c in c:
                if item_b == item_c:
                    match_c = True
                    break
        
        if not match_a and not match_c:
            print(item_b)





import telebot
import tradingview
import time

class telemain():
        
    def tradingconfig(self):
        self.tr = tradingview.tradingview_main()
        self.bot = telebot.TeleBot('6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI')

    
    def start(self):
        @self.bot.message_handler(commands=['run'])
        def echo_message(message):
           
            self.bot.send_message(message.chat.id,"Bot has started")
            self.tr.run_main()
            
            # A
            
            btc = self.tr.color_ident_bt()
            bn  = self.tr.color_ident_bn()
            eur = self.tr.color_ident_eur()
            a = [btc, bn, eur]
            
            btcef_a = self.tr.col_btcusd_ef
            bnef_a  = self.tr.col_bn_ef
            euref_a = self.tr.col_eurusd_ef
            
            a1 = [btcef_a, bnef_a, euref_a]
            
            print("\n")
            for i in a:
                #print(i)
                if i != "AVOID":
                    print(i)
                    #self.bot.send_message(message.chat.id,i)
                    
            #time.sleep(171) # 3.5 mins
            time.sleep(60)
            
            print("\n")
            c1 = None
            
            while True:
                # B
                #time.sleep(3600) # 1 hr
                time.sleep(60)
                print("1 Hr completed ",time.ctime(time.time()))
                self.tr.run_main()
                
                btc1 = self.tr.color_ident_bt()
                bn1  = self.tr.color_ident_bn()
                eur1 = self.tr.color_ident_eur()
                b = [btc1, bn1, eur1]
                
                btcef_b = self.tr.col_btcusd_ef
                bnef_b  = self.tr.col_bn_ef
                euref_b = self.tr.col_eurusd_ef
                b1 = [btcef_b, bnef_b, euref_b]
                
                for item_b in b:
                    if item_b != "AVOID":
                        match_a = False
                        match_c = False
        
                    if a is not None:
                        for item_a in a:
                            if item_b == item_a:
                                match_a = True
                                break
        
                    if c is not None:
                        for item_c in c:
                            if item_b == item_c:
                                match_c = True
                                break
        
                    if not match_a and not match_c:
                        if b1 != a1 and b1 != c1:
                            print(item_b)
                        
        
                print("\n")
                
                # C
                
                #time.sleep(3600) # 1 hr
                time.sleep(120)
                print("1 Hr completed ",time.ctime(time.time()))
                
                self.tr.run_main()
                
                btc2 = self.tr.color_ident_bt()
                bn2  = self.tr.color_ident_bn()
                eur2 = self.tr.color_ident_eur()
                c = [btc2, bn2, eur2]
                
                btcef_c = self.tr.col_btcusd_ef
                bnef_c  = self.tr.col_bn_ef
                euref_c = self.tr.col_eurusd_ef
                c1 = [btcef_c, bnef_c, euref_c]
                
                for item1 in c:
                    found_match = False
                    for item in c:
                        if item1 == item:
                            found_match = True
                            break
                    if not found_match:
                        if item1 != "AVOID":
                            #print(item1)
                            if c1 != b1:
                                print(item1)
                
                a = None
                time.sleep(60)



        
# A
btc1 = "AVOID"
bn1  = "AVOID"
eur1 = "eur red"
a = [btc1, bn1, eur1]
                
btcef_a = ["green", "green","green"]
bnef_a  = ["red", "green","green"]
euref_a = ["green", "green","red"]
a1 = [btcef_a, bnef_a, euref_a]

# B
btc2 = "AVOID"
bn2  = "bn green"
eur2 = "eur green"
b = [btc2, bn2, eur2]
                
btcef_b = ["green", "green","green"]
bnef_b  = ["green", "green","green"]
euref_b = ["green", "green","green"]
b1 = [btcef_b, bnef_b, euref_b]
                
c  = None
c1 = None
      
for item_b in b:
    if item_b != "AVOID":
        match_a = False
        match_c = False
        
        if a is not None:
            for item_a in a:
                if item_b == item_a:
                    match_a = True
                    break
        
        if c is not None:
            for item_c in c:
                if item_b == item_c:
                    match_c = True
                    break
        if not match_a and not match_c:
            continue  # Skip to the next iteration if item_b is in a or c
           
# Comparison of a1 and b1 outside the loop over b
if a1 != b1:
    for i in range(len(b)):
        item_b = b[i]
        item_b1 = b1[i]
        if item_b != "AVOID":
            print(item_b) if a1[i] != b1[i] else None
else:
    for i in range(len(b)):
        item_b = b[i]
        item_b1 = b1[i]
        if item_b != "AVOID":
            print(item_b) if item_b1 != a1[i] else None




# A
btc1 = "AVOID"
bn1  = "AVOID"
eur1 = "eur red"
a = [btc1, bn1, eur1]
                
btcef_a = ["green", "green","green"]
bnef_a  = ["red", "green","green"]
euref_a = ["green", "green","green"]
a1 = [btcef_a, bnef_a, euref_a]

# B
btc2 = "AVOID"
bn2  = "bn green"
eur2 = "eur green"
b = [btc2, bn2, eur2]
                
btcef_b = ["green", "green","green"]
bnef_b  = ["green", "green","green"]
euref_b = ["green", "green","green"]
b1 = [btcef_b, bnef_b, euref_b]
                
# Let's assume either a and a1 are None or c and c1 are None
a = None
a1 = None

# C
btc2 = "AVOID"
bn2  = "bn green"
eur2 = "AVOID"
c = [btc2, bn2, eur2]
                
btcef_c = ["green", "green","green"]
bnef_c  = ["red", "green","green"]
euref_c = ["green", "green","red"]
c1 = [btcef_c, bnef_c, euref_c]


# Comparison with b
for i in range(len(b)):
    item_b = b[i]
    item_b1 = b1[i]
    
    # Skip if item_b is "AVOID"
    if item_b == "AVOID":
        continue
    
    # Check if item_b is not in list a
    if a is not None and item_b not in a:
        continue
    
    # Check if item_b is in list c
    if c is not None and item_b in c:
        # Check corresponding lists in a1 and c1
        if c1 is not None and item_b1 != c1[i]:
            print(item_b)
    else:
        # Check corresponding lists in a1 and b1
        if a1 is not None and item_b1 != a1[i]:
            print(item_b)
            
            
            
            
###

for i in range(len(a1)):
    if a1[i] != b1[i]:
        print(b[i])
 
print("\n")
for i in range(len(b1)):
    if c1[i] != b1[i]:
        if c[i] !="AVOID":
            print(c[i])


# A
btc1 = "AVOID"
bn1  = "bn red"
eur1 = "AVOID"
a = [btc1, bn1, eur1]
                
btcef_a = ["red", "green","green"]
bnef_a  = ["red", "red","red"]
euref_a = ["red", "green","green"]
a1 = [btcef_a, bnef_a, euref_a]

# B
btc2 = "AVOID"
bn2  = "bn green"
eur2 = "eur green"
b = [btc2, bn2, eur2]
                
btcef_b = ["green", "green","green"]
bnef_b  = ["green", "green","green"]
euref_b = ["green", "green","green"]
b1 = [btcef_b, bnef_b, euref_b]

# C
btc2 = "AVOID"
bn2  = "AVOID"
eur2 = "AVOID"
c = [btc2, bn2, eur2]
                
btcef_c = ["green", "green","green"]
bnef_c  = ["red", "green","green"]
euref_c = ["red", "green","green"]
c1 = [btcef_c, bnef_c, euref_c]
        

# A

# B
#B && A
for i in range(len(a1)):
    if a1[i] != b1[i]:
        if b[i] !="AVOID":
            print(b[i])

print("\n")
#C 
#C && B
for i in range(len(b1)):
    if c1[i] != b1[i]:
        if c[i] !="AVOID":
            print(c[i])
  
print("\n")
a  = None
a1 = None
#D 
#D||B && C

if a is None and a1 is None:
    for i in range(len(c1)):
        if c1[i] != b1[i]:
            if b[i] !="AVOID":
                print(b[i]) 



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException
from requests.exceptions import ConnectionError
import time,pickle,threading 


option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

def run1():
    driver1.get("https://www.youtube.com/")
    driver1.switch_to.new_window()
    driver1.get("https://www.google.com/")

def run2():
    driver2.get("https://www.amazon.in/")
    driver2.switch_to.new_window()  
    driver2.get("https://www.flipkart.com/")

def thread_run():
    one = threading.Thread(target=run1)
    two = threading.Thread(target=run2)
    
    one.start()
    two.start()
    
    one.join()
    two.join()

thread_run()



username1="MachoManiac200300" 
password1= ":341LDw%^+"

### USA CAP ELEMENTS
# A ## 46 sec |PC

# B ## 51 sec |PC 

# C ## 46 sec |PC

############################################## 

### IND CAP ELEMENTS
# A ## 34 sec |PC

# B ## 41 sec |PC 

# C ## 34 sec |PC



################ A #####################
bot.start() #9:15

sleep(180) # 3 mins
run1 #9:18 
aa  = 
aa1 =
print() #9:19

time.sleep(900) # 14 mins

run2 #9:33
a  = 
a1 = 
print() #9:34
 
########## B loop #################
#10:34
time.sleep(2640) # 1 hr wait - 16 min 

run1 #10:18
bb  = 
bb1 =
print() #10:19

time.sleep(900) # 14 min

run2 # 10:33
b  = 
b1 = 
print() #10:34

############## B END #####################
time.sleep(2640) # 1 hr wait - 16 mins

run1  #11:18
cc  = 
cc1 =
print() #11:19

time.sleep(900) # 14 mins

run2 #11:33
c  = 
c1 = 
print() #11:34




########################


import telebot
import tradingview
import time
import MT5
import schedule 


class TeleMain:
    def __init__(self):
        self.tr = tradingview.tradingview_main()
        token = "6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI"
        self.bot = telebot.TeleBot(token)
        self.mt = MT5.mt5()
        self.running = False

    def run_us(self):
        print(time.ctime(time.time()),"\nBot has started")
        self.bot.send_message(5626388450,"\nBot has started")
        us = self.tr.run_uscap()

        if us == "BTC Red" or us == "BTCusdt Red" or us == "EurUsd Red" or us == "BTC Green" or us == "BTCusdt Green" or us == "EurUsd Green":
            self.bot.send_message(5626388450,us)
            print(us)
        else:
            print("Avoid")
            self.bot.send_message(5626388450,"AVOID")
            
    def run_ind(self):
        print(time.ctime(time.time()),"\nBot has started")
        self.bot.send_message(5626388450,"\nBot has started")
        us = self.tr.run_indcap()

        if us == "BankNifty Red" or us == "Nifty Red" or us == "BankNifty Green" or us == "Nifty Green":
            self.bot.send_message(5626388450,us)
            print(us)
        else:
            print("Avoid")
            self.bot.send_message(5626388450,"AVOID")

    def bot_polling(self):
        while self.running:
            self.bot.polling()

    def stop(self):
        print("Stopping the bot...")
        self.running = False
        self.bot.stop_polling()


def schedule_bot_us():
    a = TeleMain()
    a.run_us()
    
    time.sleep(5)
    a.stop()
    time.sleep(20) 

def schedule_bot_ind():
    a = TeleMain()
    a.run_ind()
    
    time.sleep(5)
    a.stop()
    time.sleep(20) 
    
    
a = TeleMain()
a.bot.send_message(5626388450,"Script has started")
print(time.ctime(time.time()))

schedule.every().hour.at(":18").do(schedule_bot_ind)
schedule.every().hour.at(":33").do(schedule_bot_us)

while True:
    schedule.run_pending()
    time.sleep(1)



# Scheduling for 9:00 AM to 3:15 PM, Monday to Friday
def schedule_ind():
    for hour in range(9, 17):  # from 9:00 to 16:00
        schedule.every().monday.at(f"{hour:02d}:18").do(schedule_bot_ind)
        schedule.every().tuesday.at(f"{hour:02d}:18").do(schedule_bot_ind)
        schedule.every().wednesday.at(f"{hour:02d}:18").do(schedule_bot_ind)
        schedule.every().thursday.at(f"{hour:02d}:18").do(schedule_bot_ind)
        schedule.every().friday.at(f"{hour:02d}:18").do(schedule_bot_ind)

schedule_ind()


# Scheduling for 12:00 AM to 11:30 PM, Monday to Friday
def schedule_us():
    for hour in range(0, 24):  # from 00:00 to 23:00
        schedule.every().monday.at(f"{hour:02d}:33").do(schedule_bot_us)
        schedule.every().tuesday.at(f"{hour:02d}:33").do(schedule_bot_us)
        schedule.every().wednesday.at(f"{hour:02d}:33").do(schedule_bot_us)
        schedule.every().thursday.at(f"{hour:02d}:33").do(schedule_bot_us)
        schedule.every().friday.at(f"{hour:02d}:33").do(schedule_bot_us)

schedule_us()

while True:
    schedule.run_pending()
    time.sleep(1)


"""