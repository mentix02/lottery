from django.db import models

from album.models import Album


class Upload(models.Model):

    title = models.CharField(max_length=120)
    file = models.FileField(upload_to='uploads/')
    description = models.TextField(max_length=240)
    timestamp = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=100, default='anonymous', blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='uploads')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return file.url

    class Meta:
        ordering = ('-timestamp', '-pk')
