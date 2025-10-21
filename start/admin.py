from django.contrib import admin
from start.models.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["mark", "model", "year", "color", "engine", "body_car"]
    list_filter = ["mark", "model", "year",  "color", "engine", "body_car"]


