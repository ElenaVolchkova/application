from django.conf import settings
from django.db import models

from mysite.ward.models import Ward


# from mysite.athletes.models import Athletes
# from mysite.customers.models import Customers

class Amazons(models.Model):
    ward_id = models.ForeignKey(Ward, blank=True, on_delete=models.CASCADE)
