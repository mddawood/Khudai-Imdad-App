from django.db import models

# Create your models here.
class Member(models.Model):
    pic = models.ImageField(upload_to = 'images/', blank = True, null = True)
    name = models.CharField(max_length = 200)
    designation = models.CharField(max_length = 200)
    twitter = models.URLField(blank = True, null = True)
    facebook = models.URLField(blank = True, null = True)
    linkedin = models.URLField(blank = True, null = True)

    def __str__(self):
        return self.name
