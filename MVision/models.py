from django.db import models

from django.utils import timezone
# Create your models here.
class Mvariety(models.Model):
    VISION_TYPE_CHOICE =[
        ('ML', 'MachineLearning'),
        ('DS', 'DataScience'),
        ('WD', 'WEBDEV'),
        ('UI', 'UIUX'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='visions/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=VISION_TYPE_CHOICE)

    def __str__(self):
        return self.name

