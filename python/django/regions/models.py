# -*- coding: utf-8 -*-

from django.db import models


class VisibleManager(models.Manager):
    def get_query_set(self):
        kwargs = {"visible": True}
        return super(VisibleManager, self).get_query_set().filter(**kwargs)


class region(models.Model):
    name = models.CharField(u'Регион', max_length=255)
    visible = models.BooleanField(u'Показывать?', default=True)

    allobjects = models.Manager()
    objects = VisibleManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Регион'
        verbose_name_plural = u'Регионы'


class city(models.Model):
    name = models.CharField(u'Город', max_length=255)
    visible = models.BooleanField(u'Показывать?', default=True)
    region = models.ForeignKey(region,
                               verbose_name=u"Регион")

    allobjects = models.Manager()
    objects = VisibleManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Город'
        verbose_name_plural = u'Города'
