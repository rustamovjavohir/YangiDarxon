from telegram import Update
from telegram.ext import CallbackContext

from user.models import User


def phone_entity_handler(update: Update, context: CallbackContext):
    phone_number_entity = phe = list(filter(lambda e: e.type == "phone_number", update.message.entities))[0]
    phone_number = update.message.text[phe.offset:phe.offset + phe.length]
    user_id = update.effective_user.id
    user = User.objects.filter(telegram_id=user_id).first()
    text = "Murojatlaringizni qoldiring"
    user = user.phone = phone_number
    user.save()
    context.bot.send_message(chat_id=user_id, text=text, parse_mode="HTML",
                             reply_markup=None)


def phone_contact_handler(update: Update, context: CallbackContext):
    contact = update.message.contact
    user_id = update.effective_user.id
    user = User.objects.filter(telegram_id=user_id).first()
    text = "Murojatlaringizni qoldiring"
    user.phone = contact.phone_number
    user.save()
    context.bot.send_message(chat_id=user_id, text=text, parse_mode="HTML", reply_markup=None)
