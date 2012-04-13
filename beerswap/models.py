from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

class Beer(models.Model):
    person  = models.ForeignKey(Person)
    name = models.CharField(max_length=500)
    brewery = models.CharField(max_length=500)
    rating = models.IntegerField()

    def __unicode__(self):
        return self.name
        