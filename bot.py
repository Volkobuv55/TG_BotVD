from config import token  
import telebot
import random
from random import choice 


API_TOKEN = '<api_token>'

bot = telebot.TeleBot(API_TOKEN)


list = ["Океаны покрывают около 71% поверхности Земли.","Мировой океан содержит 97% всей воды на планете.",
        "Самая высокая гора на Земле — Эверест, высота 8848 метров.","Антарктида является самым холодным местом на планете, температура может опускаться до -80°C.",
        "Сахара — это крупнейшая горячая пустыня в мире.","Древнейшие известные деревья — сосны, возраст которых достигает более 4000 лет.",
        "Медузы существуют на Земле более 500 миллионов лет.","Слон — единственное животное, которое не может прыгать.","Луна отдаляется от Земли примерно на 3,8 см в год.",
        "Калифорнийская сосна может жить до 5000 лет.","В мире более 7,9 миллиарда людей.","Наиболее распространённый язык в мире — мандаринский китайский.",
        "Самая большая пустыня на Земле — Антарктида.","Вулкан Йеллоустоун является одним из крупнейших супервулканов в мире.","Человеческий мозг состоит на 75% из воды.",
        "Свет от Солнца достигает Земли за 8 минут и 20 секунд.","Киты могут петь песни, которые слышны на расстоянии до 800 километров.",
        "Вода — единственное вещество, которое может существовать в трех состояниях: твердом, жидком и газообразном.","Скорость света составляет примерно 299,792 километров в секунду.",
        "В мире существует более 2000 различных языков.","Медузы не имеют мозга, сердца и костей."]

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['info'])
def send_welcome_1(message):
    bot.reply_to(message, (random.choice(list)) and "I am a Telegram bot named after my creator Volkobuv, at the moment I can only do a couple of things, reply to you with your own message, tell you about myself and send you interesting facts, I will be glad to work with you!")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()


