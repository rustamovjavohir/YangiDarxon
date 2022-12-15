from django.db import models


# Create your models here.


class Advertising(models.Model):
    title = models.CharField(max_length=250, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='Advertising', null=True, blank=True, verbose_name="Rasm")
    description = models.TextField(null=True, blank=True, verbose_name="Qisqacha tasnif")
    created_at = models.DateField(auto_now_add=True, verbose_name="Yaratilgan sana")
    finished_at = models.DateField(null=True, blank=True, verbose_name="Tugash sanasi")
    is_deleted = models.BooleanField(default=False, verbose_name="O'chirilgan")

    class Meta:
        ordering = ['-id']
        verbose_name = "Reklama"
        verbose_name_plural = "Reklamalar"

    def __str__(self):
        return self.title
