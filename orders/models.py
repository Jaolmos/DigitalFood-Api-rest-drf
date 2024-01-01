from django.db import models

status_enum = (   
    ('pending', 'pending'),
    ('delivered', 'delivered'),
)

class Order(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=200, choices=status_enum)
    created_at = models.DateTimeField(auto_now_add=True)
    order_is_closed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table)
    
