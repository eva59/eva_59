import telebot as tb
from telebot import types
from core.settings import settings
from core.Buttons import Buttons
from core.consts import choose, back

from schedule import ScheduleFolk,  ScheduleString , WeekDays

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
        bot.send_message(message.chat.id,choose,reply_markup=markup1)

        if call.data == 'day':
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup2.add(Buttons.monday, Buttons.tuesday, Buttons.wednesday, Buttons.thursday, Buttons.friday,Buttons.saturday, Buttons.back)
            bot.send_message(message.chat.id,choose,reply_markup=markup2)

            if call.data == 'monday':
                bot.send_message(message.chat.id,ScheduleFolk.monday,reply_markup=2)

            elif call.data == 'tuesday':
                bot.send_message(message.chat.id,ScheduleFolk.tuesday,reply_markup=2)

            elif call.data == 'wednesday':
                bot.send_message(message.chat.id,ScheduleFolk.wednesday,reply_markup=2)

            elif call.data == 'thursday':
                bot.send_message(message.chat.id,ScheduleFolk.thursday,reply_markup=2)

            elif call.data == 'friday':
                bot.send_message(message.chat.id,ScheduleFolk.friday,reply_markup=2)
            
            elif call.data == 'saturday':
                bot.send_message(message.chat.id,ScheduleFolk.saturday,reply_markup=2)
            
            elif call.data == 'back':
                bot.send_message(message.chat.id, back,reply_markup=1)

        elif call.data =='week':
            bot.send_message(message.chat.id,WeekDays.monday,ScheduleFolk.monday,WeekDays.tuesday,ScheduleFolk.tuesday,WeekDays.wednesday,ScheduleFolk.wednesday,WeekDays.thursday,ScheduleFolk.thursday,WeekDays.friday,ScheduleFolk.friday,WeekDays.saturday,ScheduleFolk.saturday,reply_markup=markup1)
            markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup4.add(Buttons.back)
            bot.send_message(message.chat.id, back,reply_markup=1)
             
    elif call.data == 'string':
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup4.add(Buttons.daily_schedule, Buttons.weekly_schedule)
        bot.send_message(message.chat.id,choose,reply_markup=markup1)
       

        if call.data == 'day':
            markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup5.add(Buttons.monday, Buttons.tuesday, Buttons.wednesday, Buttons.thursday, Buttons.friday,Buttons.saturday, Buttons.back)
            bot.send_message(message.chat.id,choose,reply_markup=5)

            if call.data == 'monday':
                bot.send_message(message.chat.id,ScheduleString.monday,reply_markup=5)

            elif call.data == 'tuesday':
                bot.send_message(message.chat.id,ScheduleString.tuesday,reply_markup=5)

            elif call.data == 'wednesday':
                bot.send_message(message.chat.id,ScheduleString.wednesday,reply_markup=5)

            elif call.data == 'thursday':
                bot.send_message(message.chat.id,ScheduleString.thursday,reply_markup=5)

            elif call.data == 'friday':
                bot.send_message(message.chat.id,ScheduleString.friday,reply_markup=5)
            
            elif call.data == 'saturday':
                bot.send_message(message.chat.id,ScheduleString.saturday,reply_markup=5)
            
            elif call.data == 'back':
                bot.send_message(message.chat.id, back,reply_markup=4)

        elif call.data =='week':
            bot.send_message(message.chat.id,WeekDays.monday,ScheduleString.monday,WeekDays.tuesday,ScheduleString.tuesday,WeekDays.wednesday,ScheduleString.wednesday,WeekDays.thursday,ScheduleString.thursday,WeekDays.friday,ScheduleString.friday,WeekDays.saturday,ScheduleString.saturday,reply_markup=markup4)
            markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup4.add(Buttons.back)
            bot.send_message(message.chat.id, back,reply_markup=4)
    
    elif call.data == 'back':
        bot.send_message(message.chat.id, back,reply_markup=None)

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
