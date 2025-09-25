from telegram.ext import CommandHandler
from telegram import Update
from KeyboardMarkup import Keyboard
from telegram.ext import CallbackContext
from ShwartsList import SwartzList
import Text


class Command:

    def __init__(self):
        self.keyboard = Keyboard()
        self.shwartz_list = SwartzList()


    async def start(self, update: Update, context):
        await update.message.reply_text(Text.TEXT_START,
                                        reply_markup=self.keyboard.reply_markup)

    async def contact_me(self, update: Update, context: CallbackContext):
        user = update.message.from_user
        username = user.username
        user_id = user.id
        first_name = user.first_name
        last_name = user.last_name
        if self.shwartz_list.check_in_swartz(user_id):
            await update.message.reply_text(Text.TEXT_FOR_USER_IN_SWARTZ)
        else:
            self.shwartz_list.add_in_list(user_id)
            await update.message.reply_text(Text.TEXT_ANSWER)
            await context.bot.send_message(chat_id=345484278,
                                           text=f'{username} - Никнейм\n'
                                                f'{first_name} - Имя\n'
                                                f'{last_name} - Фамилия',
                                           reply_markup=self.keyboard.reply_inline_markup(callback_data=user_id))

    async def processing_client(self, update: Update, context: CallbackContext):
        query = update.callback_query
        if query.data is not "done":
            user_id = int(query.data)
            self.shwartz_list.out_swartz(user_id)
            await query.answer(text='Этот человек снова может отправить тебе заявку', show_alert=False)
            new_markup = self.keyboard.reply_inline_markup(text="✅", callback_data="done")
            await query.edit_message_reply_markup(reply_markup=new_markup)
        else:
            await query.answer(text='Не дрочи кнопку ебень', show_alert=False)



