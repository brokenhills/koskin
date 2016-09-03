# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

SHORT_TEXT_LEN = 200

class Writings(models.Model):
    idwr = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name=u"Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name=u"Название")
    genre = models.CharField(max_length=20, verbose_name=u"Жанр")
    datewr = models.DateField(null=False, verbose_name=u"Дата написания")
    datead = models.DateField(auto_now_add=True, verbose_name=u"Дата загрузки")
    content = models.TextField(verbose_name=u"Текст")
    description = models.TextField(verbose_name=u"Комментарий")

    class Meta:
        verbose_name=u"Произведение"
        verbose_name_plural=u"Произведения"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content

    def get_short_text(self):
        if len(self.content) > SHORT_TEXT_LEN:
            return self.content[:SHORT_TEXT_LEN]
        else:
            return self.content
