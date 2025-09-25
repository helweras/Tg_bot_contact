from telegram.ext import CommandHandler
from telegram import Update
from KeyboardMarkup import Keyboard
from telegram.ext import CallbackContext
import Text


class Command:

    def __init__(self):
        self.keyboard = Keyboard()

    async def start(self, update: Update, context):
        await update.message.reply_text(Text.TEXT_START,
                                        reply_markup=self.keyboard.reply_markup)
    @staticmethod
    async def contact_me(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.username
        first_name = user.first_name
        await update.message.reply_text(Text.TEXT_ANSWER)
        await context.bot.send_message(chat_id=345484278,
                                       text=f'{user_id} - username\n'
                                            f'{first_name} - first_name')
