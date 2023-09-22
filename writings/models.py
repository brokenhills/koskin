# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

SHORT_TEXT_LEN = 200


@models.TextField.register_lookup
@models.CharField.register_lookup
class Search(models.Lookup):
    lookup_name = 'search'

    def as_mysql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return 'MATCH (%s) AGAINST (%s IN BOOLEAN MODE)' % (lhs, rhs), params


class Writings(models.Model):
    idwr = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    genre = models.CharField(max_length=20, verbose_name="Жанр")
    datewr = models.DateField(null=False, verbose_name="Дата написания")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")
    content = models.TextField(verbose_name="Текст")
    description = models.TextField(verbose_name="Комментарий")
    is_liked = models.BooleanField(default=0, verbose_name="Избранное")

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content

    def get_short_text(self):
        if len(self.content) > SHORT_TEXT_LEN:
            return self.content[:SHORT_TEXT_LEN]
        else:
            return self.content

    def get_liked(self):
        if self.is_liked:
            return self.name
