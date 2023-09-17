from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='employe/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
