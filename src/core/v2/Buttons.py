from enum import Enum
from telebot.types import InlineKeyboardButton


# from pydantic import BaseModel  # noqa


class Buttons(Enum):
    string_schedule = InlineKeyboardButton("Узнать расписание Струнники", callback_data= 'strunn')
    folk_schedule = InlineKeyboardButton("Узнать расписание Народники", callback_data= 'folk')
    daily_schedule = InlineKeyboardButton("Узнать расписание на день", callback_data= 'day')
    weekly_schedule = InlineKeyboardButton("Узнать расписание на неделю", callback_data= 'week')
    back = InlineKeyboardButton("Назад", callback_data = 'back')
    monday = InlineKeyboardButton("Понедельник", callback_data ='monday')
    tuesday = InlineKeyboardButton("Вторник", callback_data ='tuesday')
    wednesday = InlineKeyboardButton("Среда", callback_data =' wednesday')
    thursday = InlineKeyboardButton("Четверг", callback_data ='thursday')
    friday = InlineKeyboardButton("Пятница", callback_data ='friday')
    saturday = InlineKeyboardButton("Суббота", callback_data ='saturday')