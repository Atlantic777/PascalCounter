from django.db import models
from datetime import datetime

# Create your models here.
class Session(models.Model):
    date = models.DateTimeField(default=datetime.now())
    counter = models.IntegerField(default=0)

    def increase(self):
        self.counter += 1
        self.save()

