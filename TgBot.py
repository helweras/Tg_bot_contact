from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from Command import Command



class TgBot:
    def __init__(self):
        self.token = '8417636949:AAEZFyezBGAYd5_xqstANloEoZqH2NLqUjc'
        self.admin = '345484278'
        self.command = Command()
        self.app = Application.builder().token(self.token).build()
        self.add_handler()

    def add_handler(self):
        self.app.add_handler(CommandHandler('start', self.command.start))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.command.contact_me))
        self.app.add_handler(CallbackQueryHandler(self.command.processing_client))




    def strat_app(self):
        self.app.run_polling()


