from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='categories')
   
    def __str__(self):
        return self.title


