from django.db import models


class Sale(models.Model):
    medicines = models.ForeignKey('Medicines', on_delete=models.CASCADE)
    sale_date = models.DateField()
    quantity_sold = models.PositiveIntegerField()

    def __str__(self):
        return f'Sale of {self.medicines} on {self.sale_date}'