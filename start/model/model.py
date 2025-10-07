from django.db import models


class category(models.model):
    mark = models.CharField("mark", max_length=20)
    model = models.CharField("model", max_length=20)
    year = models.IntegerField("year")


    def __str__(self):
        return f"{self.mark} {self.model} ({self.year})"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"