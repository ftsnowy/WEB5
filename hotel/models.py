from django.db import models

# Create your models here.
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def str(self):
        return self.name


class Rooms(models.Model):
    category = models.ForeignKey(Categories, related_name='items', on_delete=models.CASCADE)
    number = models.IntegerField(default=0, null=True, blank=True)
    capacity = models.IntegerField(default=0, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True)
    is_busy = models.BooleanField(default=False)

    def str(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url