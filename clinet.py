import os
import telebot

# टेलीग्राम बॉट टोकन एनवायरनमेंट वेरिएबल से उठाएगा
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

class PowerMuslimBot:
    def __init__(self):
        print("POWER MUSLIM BOT Initialized!")

    def start(self):
        print("Bot is running... Listening for messages.")
        
        # स्टार्ट कमांड
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.reply_to(message, "✨ POWER MUSLIM BOT ✨\n\nAssalamu Alaikum! Main aapki khidmat mein hazir hoon. Commands dekhne ke liye ..status type karein.")
        
        # स्टेटस कमांड (आपके लिस्ट के हिसाब से)
        @bot.message_handler(commands=['status'])
        def send_status(message):
            bot.reply_to(message, "🛡️ Bot Status: Online\nAll systems working perfectly.")
            
        # पिंग कमांड
        @bot.message_handler(commands=['ping'])
        def send_ping(message):
            bot.reply_to(message, "Pong! 🏓 Bot active hai.")

        # यहाँ आप आगे और कमांड्स जोड़ सकते हैं (namaz, quran, etc.)
        
        # बॉट को चालू रखने के लिए
        bot.infinity_polling()

def build_application():
    return PowerMuslimBot()
