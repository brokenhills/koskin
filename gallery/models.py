# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Gallery(models.Model):
    idim = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    img = models.FileField(upload_to='photo/', null=False, verbose_name="Фотография")
    comment = models.TextField(null=False, verbose_name="Содержание")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.comment
