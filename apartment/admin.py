from django.contrib import admin

from apartment.models import *


# Register your models here.

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "filial", "room_quantity", "area", "floor", "price", "image_3d", "image_2d", "image"]
    list_display_links = ["room_quantity", "floor"]
    list_filter = ["filial", "room_quantity", "floor"]


@admin.register(Filial)
class FloorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "location"]
    list_display_links = ["name"]
