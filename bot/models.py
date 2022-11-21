from django.db import models


# Create your models here.

class BotConfig(models.Model):
    telegram_id = models.BigIntegerField(unique=True, verbose_name="Gruppa telegramId")

    class Meta:
        verbose_name = "Bot Config"
        verbose_name_plural = "Bot Config"
