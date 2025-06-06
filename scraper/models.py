from django.db import models

# Create your models here.
class Anchors(models.Model):
    name = models.CharField(max_length=500, blank=True)
    href = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.name} : '{self.href}' "