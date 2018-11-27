"""
Definition of models.
"""

from django.db import models


class Product(models.Model):
    name = models.TextField()
    price = models.TextField()
    link = models.TextField()
    objects=models.Manager()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

   # class Meta:
    #    db_table=db_table