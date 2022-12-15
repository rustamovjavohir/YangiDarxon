import requests
from django.shortcuts import render
from rest_framework.response import Response
from telegram import Update, Bot
from telegram.ext import CallbackContext

from bot.keyboards import sendPhone
from bot.models import BotConfig
from bot.serializers import SendMessageBotSerializer
from user.models import User
from rest_framework.views import APIView
from django.conf import settings


def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user = User.objects.filter(telegram_id=user_id).first()
    text = "Murojatlaringizni qoldiring"
    button = None
    if user is None:
        User.objects.create(telegram_id=user_id, name=update.message.from_user.full_name,
                            is_telegram=True)
        text = f"Hush kelibsiz {update.message.from_user.full_name}\n" \
               f"Siz bilan bog'lanishimiz uchun ma'lumotlaringizni kiriting"
        button = sendPhone()
    update.message.reply_text(text=text, reply_markup=button)


def main_handler(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    group_id = BotConfig.objects.first().telegram_id
    user = User.objects.filter(telegram_id=user_id).first()
    text = f"@{update.message.from_user.username}\n" \
           f"Ism: {user.name}\n" \
           f"Nomer: {user.phone}\n" \
           f"Xabar: {update.message.text}"

    context.bot.send_message(chat_id=group_id, text=text)
    update.message.reply_text(text="Xabaringiz jo'natildi\n"
                                   "Siz bilan tez orada bog'lanishadi")


class SendMessageView(APIView):
    serializer = SendMessageBotSerializer

    def post(self, request):
        group_id = BotConfig.objects.first().telegram_id
        self.serializer(data=request.data).is_valid(raise_exception=True)
        data = self.serializer(data=request.data).initial_data
        data.update({"chat_id": group_id})
        text = f'Mijoz: {data.get("text")}\n' \
               f'Telefon nomer: {data.get("phone")}'
        data.update({"text": text})

        response = requests.post(url=f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage", data=data)
        return Response(data=response.json())
