from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT='DF','DRAFT'
        PUBLISHED='PB','PUBLISHED'

    title=models.CharField(max_length=30)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    staus=models.CharField(max_length=10,choices=Status.choices,default=Status.DRAFT)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish'])]

    def __str__(self):
        return  f"{self.title}"
