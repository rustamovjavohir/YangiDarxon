from django.conf import settings
from django.core.management import BaseCommand
from telegram import MessageEntity
from telegram.ext import (Updater, Dispatcher, CommandHandler, CallbackQueryHandler, MessageHandler, Filters)

from bot.utils import phone_entity_handler, phone_contact_handler
from bot.views import start, main_handler


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM_TOKEN)
        dispatcher: Dispatcher = updater.dispatcher
        updater.dispatcher.add_handler(CommandHandler(command='start', callback=start))
        dispatcher.add_handler(MessageHandler(Filters.text & Filters.entity(MessageEntity.PHONE_NUMBER),
                                              callback=phone_entity_handler))
        dispatcher.add_handler(MessageHandler(Filters.contact, callback=phone_contact_handler))
        dispatcher.add_handler(MessageHandler(Filters.all, callback=main_handler))
        updater.start_polling()
        updater.idle()
