from django.db import models

# Create your models here.

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by migrations

class Contact(models.Model):
    name = models.CharField(max_length=100)
    registration = models.CharField(max_length=100)
    branch = models.CharField(max_length=10)
    roll = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.name
class AnswerPage(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name