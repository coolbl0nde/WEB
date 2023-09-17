from django.db import models
from django.utils import timezone


class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    def is_valid(self):
        now = timezone.now()
        return self.valid_from <= now <= self.valid_to
