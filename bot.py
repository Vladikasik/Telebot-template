import telebot
import config

class Bot():

    def __init__(self):

        self.bot = telebot.TeleBot(config.token)

    def mainloop(self):

        @self.bot.message_handler(commands=['start'])
        def start(msg):

            if msg.text.startswith('/start'):
                self.bot.send_message(msg.chat.id, 'Привет')
        
        self.bot.polling()

if __name__ == '__main__':
    bot = Bot()
    bot.mainloop()