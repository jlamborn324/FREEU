from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ItemPost(models.Model):
    title = models.CharField(max_length=100)
    item_image = models.ImageField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20)
