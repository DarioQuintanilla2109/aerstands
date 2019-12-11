from django.db import models
from datetime import datetime
from lessors.models import Lessor

ENUM = [("yes", "yes"),
        ("no", "no")]

class Inventory(models.Model):
    # Inventory Table
    lessor = models.ForeignKey(Lessor, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    serial_num = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=400)
    OEM_approved = models.CharField(max_length=3, choices=ENUM, default="yes")
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=100)
    length = models.IntegerField()
    width = models.IntegerField()
    depth = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_available = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.model
