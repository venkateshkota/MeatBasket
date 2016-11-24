from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Items(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=100)

    class Meta:
        db_table = u'items'
    def __unicode__(self):
        return self.title
