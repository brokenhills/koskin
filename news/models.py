# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class News(models.Model):
    idns = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    content = models.TextField(verbose_name="Текст")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content
