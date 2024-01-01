from django.db import models

payment_type_enum = (
    ('Cash', 'Cash'),
    ('Card', 'Card'),
)

status_payment_enum = (
    ("Pending", "Pending"),
    ("Paid", "Paid"),
)

class Payment(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.SET_NULL, null=True, blank=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=200, choices=payment_type_enum)
    status_payment = models.CharField(max_length=200, choices=status_payment_enum)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.table)