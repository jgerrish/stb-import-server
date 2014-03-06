from django.db import models

# Create your models here.

class Bill(models.Model):
    name = models.CharField(max_length=255)
    bill_type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
