from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
   
    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('indigo_blog:detail', kwargs={'pk': self.pk})


class Project(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('indigo_blog:project_post', kwargs={'pk': self.pk})


admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Tag)