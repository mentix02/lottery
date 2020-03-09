from django.db import models
from django.urls import reverse


class Album(models.Model):

    name = models.CharField(max_length=100)
    private = models.BooleanField(default=False)
    description = models.TextField(max_length=250, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=100, default='anonymous', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('album:detail', args=[str(self.id)])

    class Meta:
        ordering = ('-timestamp', '-pk')
