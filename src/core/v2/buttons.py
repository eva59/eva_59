from telebot.types import KeyboardButton

# from pydantic import BaseModel  # noqa


class Buttons(Enum):
    string_schedule = KeyboardButton("Узнать расписание Струнники", callback_data= 'string')
    folk_schedule = KeyboardButton("Узнать расписание Народники", callback_data= 'folk')
    daily_schedule = KeyboardButton("Узнать расписание на день", callback_data= 'day')
    weekly_schedule = KeyboardButton("Узнать расписание на неделю", callback_data= 'week')
    back = KeyboardButton("Назад", callback_data = 'back')
    monday = KeyboardButton("Понедельник")
    tuesday = KeyboardButton("Вторник")
    wednesday = KeyboardButton("Среда")
    thursday = KeyboardButton("Четверг")
    friday = KeyboardButton("Пятница")
    saturday = KeyboardButton("Суббота")