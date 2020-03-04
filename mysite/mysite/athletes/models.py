from django.conf import settings
from django.db import models
from mysite.ward.models import Ward


class Athletes(models.Model):
    ward_id = models.ForeignKey(Ward, blank=True, on_delete=models.CASCADE)
    month_1 = models.BooleanField(default=False)
    month_2 = models.BooleanField(default=False)
    month_3 = models.BooleanField(default=False)
    month_4 = models.BooleanField(default=False)
