from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.SET_NULL, null=True, blank=True)
    image = CloudinaryField('image')
    caption = models.TextField()
    created_date =models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.caption

    def display_post(cls):

        post = cls.objects.all() 
        return post
