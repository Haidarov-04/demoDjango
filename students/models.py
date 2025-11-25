from django.db import models
from start.models.models import Category 

# Create your models here.

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("name", max_length=20)
    age = models.IntegerField("age")
    phone = models.CharField("phone", max_length=20, null=True, blank=True)
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        related_name="student",
        default=1
    )

    def __str__(self):
        return f"{self.name} ({self.category.mark} {self.category.model})"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
