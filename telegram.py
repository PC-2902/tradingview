# url   : https://core.telegram.org/bots/api
# id    : ID
# token : Token
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
        self.bot = telebot.TeleBot(token)
        self.mt = MT5.mt5()
        self.running = False

    def run_us(self):
        print(time.ctime(time.time()),"\nBot has started")
        self.bot.send_message(<User-id>,"\nBot has started")
        
        us = self.tr.run_uscap()

        for i in us:
            if i != "avoid":
                print(i)
                self.bot.send_message(<User-id>,us)
            
    def run_ind(self):
        print(time.ctime(time.time()),"\nBot has started")
        self.bot.send_message(<User-id>,"\nBot has started")
        
        us = self.tr.run_indcap()

        for i in us:
            if i != "avoid":
                print(i)            
                self.bot.send_message(<User-id>,us)

    def bot_polling(self):
        while self.running:
            self.bot.polling()

    def stop(self):
        print("Stopping the bot...")
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
        print("Check Internet")
        print(e)


def schedule_bot_ind():
    
    try:
        a = TeleMain()
        a.run_ind()
    
        time.sleep(5)
        a.stop()
        time.sleep(20) 
    except Exception as e:
        print("Check Internet")
        print(e)



#schedule_bot_us()
#schedule_bot_ind()


telebot.TeleBot("Token").send_message(<User-id>,"Script has started")
print(time.ctime(time.time()))

def schedule_ind():
    for hour in range(9, 17):  # from 9:00 to 16:00
        schedule.every().monday.at(f"{hour:02d}:18").do(schedule_bot_ind)
        schedule.every().tuesday.at(f"{hour:02d}:18").do(schedule_bot_ind)
        schedule.every().wednesday.at(f"{hour:02d}:18").do(schedule_bot_ind)
        schedule.every().thursday.at(f"{hour:02d}:18").do(schedule_bot_ind)
        schedule.every().friday.at(f"{hour:02d}:18").do(schedule_bot_ind)


# Scheduling for 12:00 AM to 11:30 PM, Monday to Friday
def schedule_us():
    for hour in range(0, 24):  # from 00:00 to 23:00
        schedule.every().monday.at(f"{hour:02d}:33").do(schedule_bot_us)
        schedule.every().tuesday.at(f"{hour:02d}:33").do(schedule_bot_us)
        schedule.every().wednesday.at(f"{hour:02d}:33").do(schedule_bot_us)
        schedule.every().thursday.at(f"{hour:02d}:33").do(schedule_bot_us)
        schedule.every().friday.at(f"{hour:02d}:33").do(schedule_bot_us)


schedule_ind()
schedule_us()

while True:
    schedule.run_pending()
    time.sleep(1)

























    


    
    



    




