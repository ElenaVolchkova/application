from django.conf import settings
from django.db import models
from mysite.ward.models import Ward


class Customers(models.Model):
    ward_id = models.ForeignKey(Ward, blank=True, on_delete=models.CASCADE)
    day_1 = models.BooleanField(default=False)
    day_2 = models.BooleanField(default=False)
    day_3 = models.BooleanField(default=False)
    day_4 = models.BooleanField(default=False)
    day_5 = models.BooleanField(default=False)
    day_6 = models.BooleanField(default=False)
