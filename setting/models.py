from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to = "logo/")
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    