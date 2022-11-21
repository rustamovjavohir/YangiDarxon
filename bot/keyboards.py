from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def sendPhone():
    button = [
        [
            KeyboardButton("Telefon nomer", request_contact=True),
    ]
    ]

    return ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)
