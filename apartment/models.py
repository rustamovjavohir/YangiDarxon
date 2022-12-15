from django.db import models


# Create your models here.


class Filial(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-id"]
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"


class Apartment(models.Model):
    room_quantity = models.IntegerField(null=True, blank=True, verbose_name="Xonalar soni")
    area = models.FloatField(null=True, blank=True, verbose_name="Maydoni")
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Filial")
    floor = models.IntegerField(null=True, blank=True, verbose_name="Qavat")
    price = models.BigIntegerField(null=True, blank=True, verbose_name="Narxi")
    balcony = models.FloatField(null=True, blank=True, verbose_name="Balkon (m2)")
    bedroom = models.FloatField(null=True, blank=True, verbose_name="Yotoqxona (m2)")
    bathroom = models.FloatField(null=True, blank=True, verbose_name="Hammom (m2)")
    hall = models.FloatField(null=True, blank=True, verbose_name="Zal (m2)")
    kitchen = models.FloatField(null=True, blank=True, verbose_name="Oshxona (m2)")
    dining_room = models.FloatField(null=True, blank=True, verbose_name="Dining room (m2)")
    living_room = models.FloatField(null=True, blank=True, verbose_name="Mehmonxona (m2)")
    image = models.ImageField(upload_to='Images', null=True, blank=True, verbose_name="Rasm")
    image_2d = models.ImageField(upload_to='2DImages', null=True, blank=True, verbose_name="Rasm 2D")
    image_3d = models.ImageField(upload_to='3DImages', null=True, blank=True, verbose_name="Rasm 3D")
    is_deleted = models.BooleanField(default=False, verbose_name="O'chirilgan")

    def __str__(self):
        return f"{self.floor} qavat {self.room_quantity} {self.area}"

    class Meta:
        ordering = ["-id"]
        verbose_name = "Xonadon"
        verbose_name_plural = "Xonadonlar"
