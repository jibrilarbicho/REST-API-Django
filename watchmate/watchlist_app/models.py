from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    wesbite = models.URLField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchlist"
    )
    storyline = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
