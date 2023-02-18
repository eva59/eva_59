import telebot as tb
from telebot import types
from ..settings import settings
from utils import Buttons 
#ScheduleFolk, WeekDays, ScheduleString, 

bot = tb.TeleBot(settings.telegram_token.get_secret_value())


@bot.message_handler(commands=["start"])
def start(message):
    markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = tb.types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(
        message.from_user.id, "Привет! Я твой бот-помошник!", reply_markup=markup
    )
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(Buttons.folk_schedule, Buttons.string_schedule)
        bot.send_message(message.from_user.id, 'Выберете действие', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def answer(call,message):
    if call.data == 'folk':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup1.add(Buttons.daily_schedule, Buttons.weekly_schedule)
        bot.send_message(message.chat.id,"Выберите,что вам нужно,если хотите вернуться в меню просто нажмите кнопку 'Назад в меню' ",reply_markup=markup1)
    
    elif call.data == 'string':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup2.add(Buttons.daily_schedule, Buttons.weekly_schedule)
        bot.send_message(message.chat.id,"Выберите,что вам нужно,если хотите вернуться в меню просто нажмите кнопку 'Назад в меню' ",reply_markup=markup1)
    
    elif call.data == 'back':
        bot.send_message(message.chat.id, "Вы вернулись в меню",reply_markup=None)

    










@bot.message_handler(
    func=lambda message: True,
    content_types=[
        "audio",
        "photo",
        "voice",
        "video",
        "document",
        "text",
        "location",
        "contact",
        "sticker",
    ],
)
def default_command(message):
    bot.send_message(message.chat.id, "Invalid command")
