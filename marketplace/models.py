from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import json
import base64

def linkconverter(oldlink):
    imagerequest = {
        "bucket":"freeu-images",
        "key": oldlink, 
        "edits": {
            "resize": {"width":100}
        }
    }
    imagerequest = json.dumps(imagerequest, separators=(",", ":"))
    imagerequest = imagerequest.encode("utf-8")
    newlink = base64.b64encode(imagerequest)
    newlink = newlink.decode("utf-8")
    return "https://dsv856zfdr0u5.cloudfront.net/" + newlink

class ItemPost(models.Model):
    title = models.CharField(max_length=100)
    item_image = models.ImageField(blank=True, null=True)
    link = linkconverter(str(item_image))

    

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20)

    def __str__(self): 
        return self.title

    def get_new_url(self):
        link = linkconverter(str(self.item_image))
        return link
    
    def get_absolute_url(self):
        return reverse('itempost-detail', kwargs= {'pk': self.pk})
 




