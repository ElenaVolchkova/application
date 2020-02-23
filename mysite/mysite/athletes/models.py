from django.conf import settings
from django.db import models
from mysite.ward.models import Ward


class Athletes(models.Model):
    ward_id = models.ForeignKey(Ward, blank=True, on_delete=models.CASCADE)
