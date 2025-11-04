from django.contrib import admin
from students.models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "phone", "mail"]
    list_filter = ["name", "age", "phone", "mail"]



