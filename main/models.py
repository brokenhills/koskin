# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Main(models.Model):
    idmn = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    content = models.TextField(null=False, verbose_name="Текст")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content
