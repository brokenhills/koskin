# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Contact(models.Model):
    idcn = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    content = models.TextField(null=False, verbose_name="Содержание")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name="Контакты"
        verbose_name_plural="Контакты"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content
