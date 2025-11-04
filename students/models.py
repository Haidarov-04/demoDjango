from django.db import models
from start.models.models import Category 

# Create your models here.

class Students(models.Model):
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="student",
        default=1
    )
    name = models.CharField("name", max_length=20)
    age = models.IntegerField("age")
    phone = models.CharField("phone", max_length=20, null=True, blank=True)
    mail = models.CharField("mail", max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.category.mark} {self.category.model})"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"