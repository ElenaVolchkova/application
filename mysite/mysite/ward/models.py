from django.conf import settings
from django.db import models


class Ward(models.Model):
    # ward_id = models.ForeignKey(Ward, blank=True, on_delete=models.CASCADE)
    ward = models.TextField()
    id = models.AutoField(primary_key=True)
