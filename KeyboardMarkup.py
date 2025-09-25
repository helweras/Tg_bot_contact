from telegram import ReplyKeyboardMarkup, KeyboardButton


class Keyboard:
    def __init__(self):
        self.keyboard = [[KeyboardButton('Связаться со мной')]]
        self.reply_markup = ReplyKeyboardMarkup(self.keyboard, resize_keyboard=True)