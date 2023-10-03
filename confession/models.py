from django.db import models

# Create your models here.


class Confession(models.Model):
    content = models.TextField(max_length=100, blank=False, null=False)

    date = models.DateTimeField(auto_now_add=True)

    likes = models.PositiveIntegerField(default=0)

    moderated = models.BooleanField(default=False)