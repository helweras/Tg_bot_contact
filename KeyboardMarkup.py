from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from MyInlineButton import MyInlineButton


class Keyboard:
    def __init__(self):
        self.keyboard_reply = [[KeyboardButton('Связаться со мной')]]
        self.reply_markup = ReplyKeyboardMarkup(self.keyboard_reply, resize_keyboard=True)

        self.keyboard_inline = [[InlineKeyboardButton('Обработан', callback_data='ready')]]
        self.inline_markup = InlineKeyboardMarkup(self.keyboard_inline)


    # def create_inline_button(self,callback_data, user_id):
    #     return MyInlineButton(text='Обработан', callback_data=callback_data, user_id=user_id)
    #
    # def create_inline_markup(self, inline_button):
    #     return [inline_button]
    #
    # def reply_inline_markup(self, user_id, callback_data='ready'):
    #     btn = self.create_inline_button(callback_data, user_id)
    #     markup = self.create_inline_markup(btn)
    #     self.created_inline_markups.append(markup)
    #     return markup

    def create_inline_button(self, callback_data, text):
        return InlineKeyboardButton(text=text, callback_data=callback_data)

    def create_inline_markup(self, inline_button):
        return InlineKeyboardMarkup([[inline_button]])

    def reply_inline_markup(self, callback_data, text='Обработать'):
        btn = self.create_inline_button(callback_data=callback_data,text=text)
        markup = self.create_inline_markup(btn)
        return markup