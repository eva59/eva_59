from enum import Enum
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


class WeekDays(Enum):
    monday = "Понедельник"
    tuesday = "Вторник"
    wednesday = "Среда"
    thursday = "Четверг"
    friday = "Пятница"
    saturday = "Суббота"
    sunday = "Воскресенье"


class ScheduleFolk(Enum):
    monday = (
        "Вазговоры о важном - 9:00-9:45\n"
        "Оркестровый класс - 10:40-14:15"
        "(перерыв - 12:10-12:45)"
    )
    tuesday = (
        "Математика - 12:45-14:15\n"
        "Музыкальная литература - 14:25-15:55\n"
        "Литература - 16:05-17:35"
    )
    wednesday = (
        "Русский язык - 9:00-10:30\n"
        "Оркестровый класс - 10:40-14:15(перерыв - 12:10-12:45)\n"
        "Сольфеджио - 14:25-15:55\n"
    )
    thursday = (
        "История - 12:45-14:15\n"
        "ЭТМ - 14:25-15:55"
    )
    friday = (
        "Оркестровый класс - 10:40-12:10\n"
        "Музыкальная литература - 12:45-14:10\n"
        "ИМК - 16:05-17:35"
    )
    saturday = (
        "Английский - 10:40-12:10\n"
        "Естествознание - 14:25-15:55"
    )
    sunday = "Воскресенье"

class ScheduleString(Enum):
    monday = (
        "Математика - 9:00-10:30\n"
        "ИМК - 10:40-12:10\n"
        "Литература - 12:10-14:15\n"
        "ЭТМ - 14:25-15:55"
    )
    tuesday = (
        "Оркестровый класс - 14:25-17:35"
    )
    wednesday = (
        "Математика - 9:00-10:30\n"
        "ИМК - 10:40-12:10\n"
        "Литература - 12:10-14:15\n"
        "ЭТМ - 14:25-15:55"
    )
    thursday = (
        "Оркестровый класс - 10:40-13:55\n"
        "ОБЖ - 14:25-15:55"
    )
    friday = (
        "Музыкальная литература - 14:45-15:55\n"
        "Сольфеджио- 16:05-17:35"
    )
    saturday = (
        "Русский язык - 12:45-14:15\n"
        "Оркестровый класс - 14:25-17:35"
    )
    sunday = "Воскресенье"

    # bot.send_message(message.from_user.id, """Вторник: """)
    # bot.send_message(
    #     message.from_user.id,
    #     """Математика - 12:45-14:15
    # Музыкальная литература - 14:25-15:55
    # Литература - 16:05-17:35""",
    # )
    # bot.send_message(message.from_user.id, """Среда: """)
    # bot.send_message(
    #     message.from_user.id,
    #     """Русский язык - 9:00-10:30
    # Оркестровый класс - 10:40-14:15(перерыв - 12:10-12:45)
    # Сольфеджио - 14:25-15:55""",
    # )
    # bot.send_message(message.from_user.id, """Четверг: """)
    # bot.send_message(
    #     message.from_user.id,
    #     """История - 12:45-14:15
    # ЭТМ - 14:25-15:55""",
    # )
    # bot.send_message(message.from_user.id, """Пятница: """)
    # bot.send_message(
    #     message.from_user.id,
    #     """Оркестровый класс - 10:40-12:10
    # Музыкальная литература - 14:45-15:55
    # ИМК - 16:05-17:35""",
    # )
    # bot.send_message(message.from_user.id, """Суббота: """)
    # bot.send_message(
    #     message.from_user.id,
    #     """Английский - 10:40-12:10
    # Естествознание - 14:25-15:55""",
    # )
    # elif message.text == WeekDays.monday.value:
    #     bot.send_message(
    #         message.from_user.id,
    #         f"{message.text}: ",
    #     )
    #     bot.send_message(
    #         message.from_user.id,
    #         ScheduleString.monday.value,
    #     )
    # if 1:
    #     send_schedule(ScheduleString)
    # elif 2:
    #     schedule = ScheduleFolk
    #     send_schedule(schedule)
    # send_schedule(schedule)

    # def send_schedule(schedule: ScheduleString | ScheduleFolk) -> str:
    #     bot.send_message(
    #         message.from_user.id,
    #         f"{message.text}: ",
    #     )
    #     bot.send_message(
    #         message.from_user.id,
    #         schedule.monday.value,
    #     )

    # schedule.monday.value



