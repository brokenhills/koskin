# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

WIDTH_PREVIEW = 64
HEIGHT_PREVIEV = 48

class Gallery(models.Model):
    idim = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name=u"Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name=u"Название")
    img = models.FileField(upload_to='media/', null=False, verbose_name=u"Фотография")
    comment = models.TextField(null=False, verbose_name=u"Содержание")
    datead = models.DateField(auto_now_add=True, verbose_name=u"Дата загрузки")

    class Meta:
        verbose_name=u"Фотографии"
        verbose_name_plural=u"Фотографии"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.comment


