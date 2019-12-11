from django.db import models
from datetime import datetime

class Lessee(models.Model):
    # Lessee Table
    connect_id = models.CharField(max_length=400)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='img/avatar.jpg')
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50)
    joined_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(self.id)
