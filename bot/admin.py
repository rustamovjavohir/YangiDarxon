from django.contrib import admin
from bot.models import BotConfig


# Register your models here.

@admin.register(BotConfig)
class BotConfigAdmin(admin.ModelAdmin):
    list_display = ["id", "telegram_id"]
