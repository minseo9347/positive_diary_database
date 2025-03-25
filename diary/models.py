from django.db import models

# Create your models here.
# diary/models.py

from django.db import models

class Affirmation(models.Model):
    nickname = models.CharField(max_length=50)
    date = models.DateField()
    emotion = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.nickname} - {self.date}"
