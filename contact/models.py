# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    idcn = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name=u"Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name=u"Название")
    content = models.TextField(null=False, verbose_name=u"Содержание")
    datead = models.DateField(auto_now_add=True, verbose_name=u"Дата загрузки")

    class Meta:
        verbose_name=u"Контакты"
        verbose_name_plural=u"Контакты"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content