from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=200)
    tag = models.ManyToManyField(Tag)
    yearCreated = models.IntegerField()
    rate = models.FloatField()
    poster = models.TextField()
    trailer = models.TextField()
    IsFeatured = models.BooleanField(default=False)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.title
