from django.db import models


class Progress(models.Model):
    name = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=30)
    temp = models.FloatField(null=True, blank=True)
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
