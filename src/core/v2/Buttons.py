from enum import Enum
from telebot.types import KeyboardButton

# from pydantic import BaseModel  # noqa


class Buttons(Enum):
    string_schedule = KeyboardButton("Узнать расписание Струнники", callback_data= 'strunn')
    folk_schedule = KeyboardButton("Узнать расписание Народники", callback_data= 'folk')
    daily_schedule = KeyboardButton("Узнать расписание на день", callback_data= 'day')
    weekly_schedule = KeyboardButton("Узнать расписание на неделю", callback_data= 'week')
    back = KeyboardButton("Назад", callback_data = 'back')
    monday = KeyboardButton("Понедельник", callback_data ='monday')
    tuesday = KeyboardButton("Вторник", callback_data ='tuesday')
    wednesday = KeyboardButton("Среда", callback_data =' wednesday')
    thursday = KeyboardButton("Четверг", callback_data ='thursday')
    friday = KeyboardButton("Пятница", callback_data ='friday')
    saturday = KeyboardButton("Суббота", callback_data ='saturday')