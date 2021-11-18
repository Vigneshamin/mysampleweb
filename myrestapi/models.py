from django.db import models

class Productitems(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    photo = models.ImageField(blank=True, null=True, default=None, upload_to='products')

    def __str__(self):
        return self.name