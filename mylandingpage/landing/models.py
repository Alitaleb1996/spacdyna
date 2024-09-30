from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()

    def __self__(self):
        return f'{self.name} {self.surname}'
    