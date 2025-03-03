from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    wireframe = models.ImageField()
    trello = models.URLField(blank=True, null=True)
    case_study = models.TextField()
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name