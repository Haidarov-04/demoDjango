from django.contrib import admin
from start.models.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["mark", "model", "year"]
    list_filter = ["mark", "model", "year"]


