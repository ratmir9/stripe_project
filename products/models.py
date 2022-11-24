from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=255)
    description = models.TextField(verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Цена товара в центах', default=0)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    
    