from telegram import InlineKeyboardButton

class MyInlineButton(InlineKeyboardButton):
    def __init__(self, text, callback_data, user_id=None, **kwargs):
        super().__init__(text=text, callback_data=callback_data, **kwargs)
        self.user_id = user_id