from django.db import models


# Create your models here.


class Email(models.Model):
    subject = models.CharField(null=True, blank=True, max_length=250, verbose_name="Sarlavha")
    message = models.TextField(verbose_name="Habarnoma")
    email = models.EmailField(max_length=250, verbose_name="email")
    recipient = models.EmailField(max_length=250, null=True, blank=True, verbose_name="Telefon nomer")
    phone = models.CharField(max_length=250, null=True, blank=True, verbose_name="Jo'natuvchi")
    created_at = models.DateField(auto_now_add=True, verbose_name="Yaratilgan sana")
    is_deleted = models.BooleanField(default=False, verbose_name="O`chirilgan")

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-id"]
        verbose_name = "Email"
        verbose_name_plural = "Emaillar"
