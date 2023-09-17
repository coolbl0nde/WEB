from django.db import models


class Medicines(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    instruction = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    pharmacy_department = models.ForeignKey('PharmacyDepartment', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name