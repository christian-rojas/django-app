from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name