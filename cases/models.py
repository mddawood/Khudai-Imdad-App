from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Case(models.Model):
    img = models.ImageField(upload_to = 'images/', blank = True, null = True)
    receiver_name = models.CharField(max_length = 200, blank = True, null = True)
    description = models.TextField()
    date = models.DateField(default = timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.receiver_name

    def get_absolute_url(self):
        return reverse("cases:c_list")

class Image(models.Model):
    case = models.ForeignKey(Case, related_name='images', on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'images/', blank = True, null = True)
    number = models.CharField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return self.number
