from django.contrib import admin
from .models import ItemPost

class ItemPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "condition", "date_posted")

admin.site.register(ItemPost, ItemPostAdmin)
