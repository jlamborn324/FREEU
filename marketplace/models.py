from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ItemPost(models.Model):
    title = models.CharField(max_length=100)
    item_image = models.ImageField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20)

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self):
        return reverse('itempost-detail', kwargs= {'pk': self.pk})


