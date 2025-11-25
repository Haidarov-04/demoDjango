from django.contrib import admin
from students.models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "phone"]
    list_filter = ["id","name", "age", "phone"]



