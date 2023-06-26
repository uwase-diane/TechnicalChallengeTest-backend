from django.db import models

# Create your models here.
from django.db import models

class PageContent(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    objectives = models.TextField()

    def __str__(self):
        return "Page Content"