from django.db import models

# Create your models here.
class Subscriber(models.Model):
    useremail = models.CharField(max_length=100)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.useremail

