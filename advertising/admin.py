from django.contrib import admin
from advertising.models import Advertising


# Register your models here.
@admin.register(Advertising)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "image", "created_at", "finished_at", "is_deleted"]
    list_display_links = ['id', 'title']
