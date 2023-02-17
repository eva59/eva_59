import telebot as tb
from ..settings import settings
from utils import Buttons, ScheduleFolk, WeekDays, ScheduleString

bot = tb.TeleBot(settings.telegram_token.get_secret_value())


@bot.message_handler(commands=["start"])
def start(message):
    markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = tb.types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(
        message.from_user.id, "Привет! Я твой бот-помошник!", reply_markup=markup
    )


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "Поздороваться":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(Buttons.folk_schedule, Buttons.string_schedule)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)

    elif message.text == "Узнать расписание Народники":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(Buttons.weekly_schedule, Buttons.daily_schedule, Buttons.back)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)

    elif message.text == "Назад":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(Buttons.folk_schedule, Buttons.string_schedule)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)

    elif message.text == "Узнать расписание Струнники":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = tb.types.KeyboardButton("Узнать расписание на день")
        btn2 = tb.types.KeyboardButton("Узнать расписание на неделю")
        btn3 = tb.types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)

    elif message.text == "Узнать расписание на неделю":
        bot.send_message(
            message.from_user.id,
            """Вот ваше расписание:
                Понедельник: """,
        )
        bot.send_message(
            message.from_user.id,
            """Вазговоры о важном - 9:00-9:45
                История - 12:45-14:15
                Музыкальная литература - 14:25-15:55
                Английский - 16:05-17:35
                Естествознание - 18:10-19:40""",
        )
        bot.send_message(message.from_user.id, """Вторник: """)
        bot.send_message(message.from_user.id, """Оркестровый класс - 14:25-17:35""")
        bot.send_message(message.from_user.id, """Среда: """)
        bot.send_message(
            message.from_user.id,
            """Математика - 9:00-10:30
                ИМК - 10:40-12:10
                Литература - 12:10-14:15
                ЭТМ - 14:25-15:55""",
        )
        bot.send_message(message.from_user.id, """Четверг: """)
        bot.send_message(
            message.from_user.id,
            """Оркестровый класс - 10:40-13:55
        ОБЖ - 14:25-15:55""",
        )
        bot.send_message(message.from_user.id, """Пятница: """)
        bot.send_message(
            message.from_user.id,
            """Музыкальная литература - 14:45-15:55
                Сольфеджио- 16:05-17:35""",
        )
        bot.send_message(message.from_user.id, """Суббота: """)
        bot.send_message(
            message.from_user.id,
            """Русский язык - 12:45-14:15
                Оркестровый класс - 14:25-17:35""",
        )

    elif message.text == "Узнать расписание на день":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = tb.types.KeyboardButton("Понедельник")
        btn4 = tb.types.KeyboardButton("Вторник")
        btn5 = tb.types.KeyboardButton("Среда")
        btn6 = tb.types.KeyboardButton("Четверг")
        btn7 = tb.types.KeyboardButton("Пятница")
        btn8 = tb.types.KeyboardButton("Суббота")
        btn9 = tb.types.KeyboardButton("Назад")
        markup.add(btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)

    elif message.text == WeekDays.monday.value:
        bot.send_message(
            message.from_user.id,
            f"{message.text}: ",
        )
        bot.send_message(
            message.from_user.id,
            """Вазговоры о важном - 9:00-9:45
                История - 12:45-14:15
                Музыкальная литература - 14:25-15:55
                Английский - 16:05-17:35
                Естествознание - 18:10-19:40""",
        )

    elif message.text == "Вторник":
        bot.send_message(
            message.from_user.id,
            f"{message.text}: ",
        )
        bot.send_message(message.from_user.id, """Оркестровый класс - 14:25-17:35""")

    elif message.text == "Среда":
        bot.send_message(
            message.from_user.id,
            f"{message.text}: ",
        )
        bot.send_message(
            message.from_user.id,
            """Математика - 9:00-10:30
                ИМК - 10:40-12:10
                Литература - 12:10-14:15
                ЭТМ - 14:25-15:55""",
        )

    elif message.text == "Четверг":
        bot.send_message(
            message.from_user.id,
            f"{message.text}: ",
        )
        bot.send_message(
            message.from_user.id,
            """Оркестровый класс - 10:40-13:55
        ОБЖ - 14:25-15:55""",
        )

    elif message.text == "Пятница":
        bot.send_message(
            message.from_user.id,
            f"{message.text}: ",
        )
        bot.send_message(
            message.from_user.id,
            """ОМузыкальная литература - 14:45-15:55
                Сольфеджио- 16:05-17:35""",
        )

    elif message.text == "Суббота":
        bot.send_message(
            message.from_user.id,
            f"{message.text}: ",
        )
        bot.send_message(
            message.from_user.id,
            """Русский язык - 12:45-14:15
                Оркестровый класс - 14:25-17:35""",
        )

    elif message.text == "Назад":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = tb.types.KeyboardButton("Узнать расписание на один день")
        btn2 = tb.types.KeyboardButton("Узнать расписание на всю неделю")
        btn3 = tb.types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)

    elif message.text == "Узнать расписание Народники":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = tb.types.KeyboardButton("Узнать расписание на один день")
        btn2 = tb.types.KeyboardButton("Узнать расписание на всю неделю")
        btn3 = tb.types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)

    elif message.text == "Узнать расписание на всю неделю":
        bot.send_message(
            message.from_user.id,
            """Вот ваше расписание:
        Понедельник: """,
        )
        bot.send_message(
            message.from_user.id,
            """Вазговоры о важном - 9:00-9:45
        Оркестровый класс - 10:40-14:15(перерыв - 12:10-12:45)""",
        )
        bot.send_message(message.from_user.id, """Вторник: """)
        bot.send_message(
            message.from_user.id,
            """Математика - 12:45-14:15
        Музыкальная литература - 14:25-15:55
        Литература - 16:05-17:35""",
        )
        bot.send_message(message.from_user.id, """Среда: """)
        bot.send_message(
            message.from_user.id,
            """Русский язык - 9:00-10:30
        Оркестровый класс - 10:40-14:15(перерыв - 12:10-12:45)
        Сольфеджио - 14:25-15:55""",
        )
        bot.send_message(message.from_user.id, """Четверг: """)
        bot.send_message(
            message.from_user.id,
            """История - 12:45-14:15
        ЭТМ - 14:25-15:55""",
        )
        bot.send_message(message.from_user.id, """Пятница: """)
        bot.send_message(
            message.from_user.id,
            """Оркестровый класс - 10:40-12:10
        Музыкальная литература - 14:45-15:55
        ИМК - 16:05-17:35""",
        )
        bot.send_message(message.from_user.id, """Суббота: """)
        bot.send_message(
            message.from_user.id,
            """Английский - 10:40-12:10
        Естествознание - 14:25-15:55""",
        )

    elif message.text == "Узнать расписание на один день":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = tb.types.KeyboardButton("Понедельник")
        btn4 = tb.types.KeyboardButton("Вторник")
        btn5 = tb.types.KeyboardButton("Среда")
        btn6 = tb.types.KeyboardButton("Четверг")
        btn7 = tb.types.KeyboardButton("Пятница")
        btn8 = tb.types.KeyboardButton("Суббота")
        btn9 = tb.types.KeyboardButton("Назад")
        markup.add(btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)

    elif message.text == WeekDays.monday.value:
        bot.send_message(
            message.from_user.id,
            f"{message.text}: ",
        )
        bot.send_message(
            message.from_user.id,
            ScheduleString.monday.value,
        )

    elif message.text == "Вторник":
        bot.send_message(message.from_user.id, """Вторник: """)
        bot.send_message(
            message.from_user.id,
            """Математика - 12:45-14:15
                Музыкальная литература - 14:25-15:55
                Литература - 16:05-17:35""",
        )

    elif message.text == "Среда":
        bot.send_message(message.from_user.id, """Среда: """)
        bot.send_message(
            message.from_user.id,
            """Русский язык - 9:00-10:30
                                                Оркестровый класс - 10:40-14:15(перерыв - 12:10-12:45)
                Сольфеджио - 14:25-15:55""",
        )

    elif message.text == "Четверг":
        bot.send_message(message.from_user.id, """Четверг: """)
        bot.send_message(
            message.from_user.id,
            """История - 12:45-14:15
                ЭТМ - 14:25-15:55""",
        )

    elif message.text == "Пятница":
        bot.send_message(message.from_user.id, """Пятница: """)
        bot.send_message(
            message.from_user.id,
            """Оркестровый класс - 10:40-12:10
                Музыкальная литература - 14:45-15:55
                ИМК - 16:05-17:35""",
        )

    elif message.text == "Суббота":
        bot.send_message(message.from_user.id, """Суббота: """)
        bot.send_message(
            message.from_user.id,
            """Английский - 10:40-12:10
                Естествознание - 14:25-15:55""",
        )

    elif message.text == "Назад":
        markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = tb.types.KeyboardButton("Узнать расписание на один день")
        btn2 = tb.types.KeyboardButton("Узнать расписание на всю неделю")
        btn3 = tb.types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберете действие", reply_markup=markup)


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
