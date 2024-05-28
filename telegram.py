# url   : https://core.telegram.org/bots/api
# id    : 5626388450
# token : 6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI
# Steps : botfather > /start /mybots

"""
for chat_it :::

import telebot
import tradingview
import time
import MT5

class TeleMain:
    def __init__(self):
        self.tr = tradingview.tradingview_main()
        token = "6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI"
        self.bot = telebot.TeleBot(token)
        self.mt = MT5.mt5()
        self.start_uscap()

    def start_uscap(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle_all_messages(message):
            # Print chat ID
            chat_id = message.chat.id
            print("Chat ID:", chat_id)
            
            # Print message ID
            print("Message ID:", message.message_id)
            
            # You can add your message handling logic here
            # For example, send a response to the user
            self.bot.reply_to(message, "Received your message.")
        
        self.bot.polling()

a = TeleMain()

"""

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

        for i in us:
            a = self.mt()
            if i != "avoid":
                print(i)
                if i == "BTCusdt Green":
                    a.buy_btc_order()
            
                elif i == "BTCusdt Red":
                    a.sell_btc_order()

                elif i == "EurUsd Green":
                    a.buy_eur_order()    
            
                elif i == "EurUsd Red":
                    a.sell_eurusd()
        
                elif i == "Gold Green":
                    a.buy_gold_order()            
        
                elif i == "Gold Red":
                    a.sell_gold_order()
                
                else:
                    pass
            
    def run_ind(self):
        print(time.ctime(time.time()),"\nBot has started")
        self.bot.send_message(5626388450,"\nBot has started")
        
        us = self.tr.run_indcap()

        for i in us:
            if i != "avoid":
                print(i)            
                self.bot.send_message(5626388450,i)

    def bot_polling(self):
        while self.running:
            self.bot.polling()

    def stop(self):
        print("Stopping the bot...\n")
        self.running = False
        self.bot.stop_polling()


def schedule_bot_us():
    try:
        a = TeleMain()
        a.run_us()
    
        time.sleep(5)
        a.stop()
        time.sleep(20) 
    except Exception as e:
        print("Check Internet\nTeleBot Error")
        print(e)
        telebot.TeleBot("6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI").send_message(5626388450,e)

def schedule_bot_ind():
    
    try:
        a = TeleMain()
        a.run_ind()
    
        time.sleep(5)
        a.stop()
        time.sleep(20) 
        
    except Exception as e:
        print("Check Internet\nTeleBot Error")
        print(e)
        telebot.TeleBot("6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI").send_message(5626388450,e)



#schedule_bot_us()
#TeleMain().mt.profit()
#schedule_bot_ind()


#telebot.TeleBot("6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI").send_message(5626388450,"Script has started")
print(time.ctime(time.time()))

# Scheduling for 9:00 AM to 4:00 PM, Monday to Friday
def schedule_ind():
    for hour in range(9, 16):  # from 9:00 to 17:00
        schedule.every().monday.at(f"{hour:02d}:19").do(schedule_bot_ind)
        
        schedule.every().tuesday.at(f"{hour:02d}:19").do(schedule_bot_ind)
        
        schedule.every().wednesday.at(f"{hour:02d}:19").do(schedule_bot_ind)
        
        schedule.every().thursday.at(f"{hour:02d}:19").do(schedule_bot_ind)
        
        schedule.every().friday.at(f"{hour:02d}:19").do(schedule_bot_ind)


# Scheduling for 12:00 AM to 11:30 PM, Monday to Friday
def schedule_us():
    for hour in range(0, 24):  # from 00:00 to 23:00
        
        schedule.every().monday.at(f"{hour:02d}:34").do(schedule_bot_us)
        
        schedule.every().tuesday.at(f"{hour:02d}:34").do(schedule_bot_us)
        
        schedule.every().wednesday.at(f"{hour:02d}:34").do(schedule_bot_us)
        
        schedule.every().thursday.at(f"{hour:02d}:34").do(schedule_bot_us)
        
        schedule.every().friday.at(f"{hour:02d}:34").do(schedule_bot_us)

schedule_ind()
schedule_us()


while True:
    schedule.run_pending()
    time.sleep(1)

























    


    
    



    




