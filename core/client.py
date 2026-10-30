import os
import telebot

# टेलीग्राम बॉट टोकन एनवायरनमेंट वेरिएबल से उठाएगा
TOKEN = os.environ.get('BOT_TOKEN')

if not TOKEN:
    print("Warning: BOT_TOKEN environment variable not set!")

bot = telebot.TeleBot(TOKEN)

class PowerMuslimBot:
    def __init__(self):
        print("POWER MUSLIM BOT Initialized!")

    def start(self):
        print("Bot is running... Listening for messages.")
        
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.reply_to(message, "✨ POWER MUSLIM BOT ✨\n\nAssalamu Alaikum! Main aapki khidmat mein hazir hoon.")
        
        @bot.message_handler(commands=['status'])
        def send_status(message):
            bot.reply_to(message, "🛡️ Bot Status: Online\nAll systems working perfectly.")
            
        @bot.message_handler(commands=['ping'])
        def send_ping(message):
            bot.reply_to(message, "Pong! 🏓 Bot active hai.")

        print("Polling started...")
        bot.infinity_polling()

def build_application():
    return PowerMuslimBot()
