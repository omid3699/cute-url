from django.db import models

# Create your models here.


class Url(models.Model):
    long = models.URLField()
    short = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short}: {self.clicks}"
