from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    objective = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.PositiveIntegerField(null=True)


class Job(models.Model):

    resume = models.ForeignKey(Resume)
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def is_present(self):
        if self.end_date is None:
            return True
        return False

