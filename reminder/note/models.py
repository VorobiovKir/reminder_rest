from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User


class Colors(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.name


class Notes(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    color = models.ForeignKey(Colors, blank=True, null=True)
    tag = models.ManyToManyField(Tags, blank=True)
    category = models.ManyToManyField(Categories, blank=True)
    author = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('pub_date', )
