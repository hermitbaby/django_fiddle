from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __unicode__(self):              # __unicode__ on Python 2
        return '<%s: %s>' % (type(self).__name__, self.name)
    def __repr__(self):
        return '<%s: %s>' % (type(self).__name__, self.name)

class Author(BaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(BaseModel):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()


class Book(BaseModel):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()


class Store(BaseModel):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
