from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=250, verbose_name="F.I.SH")
    phone = models.CharField(max_length=15, verbose_name="Telefon nomer")
    message = models.TextField(blank=True, null=True, verbose_name="Habar")
    email = models.CharField(max_length=250, null=True, blank=True, verbose_name="Email")
    data = models.JSONField(default=dict)
    telegram_id = models.BigIntegerField(null=True, blank=True, verbose_name="Telegram id")
    is_telegram = models.BooleanField(default=False, verbose_name="Telegramdan")
    is_web = models.BooleanField(default=False, verbose_name="Saytdan")
    is_done = models.BooleanField(default=False, verbose_name="Javob berilgan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"
