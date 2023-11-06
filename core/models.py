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
        db_table = 'writings_writings'

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


class News(models.Model):
    idns = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    content = models.TextField(verbose_name="Текст")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        db_table = 'news_news'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content


class Main(models.Model):
    idmn = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    content = models.TextField(null=False, verbose_name="Текст")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
        db_table = 'main_main'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content


class Gallery(models.Model):
    idim = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    img = models.FileField(upload_to='photo/', null=False, verbose_name="Фотография")
    comment = models.TextField(null=False, verbose_name="Содержание")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотографии"
        db_table = 'gallery_gallery'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.comment


class Contact(models.Model):
    idcn = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    content = models.TextField(null=False, verbose_name="Содержание")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name="Контакты"
        verbose_name_plural="Контакты"
        db_table = 'contact_contact'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content


class Biography(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False, verbose_name="Идентификатор")
    name = models.CharField(max_length=40, unique=True, null=False, verbose_name="Название")
    content = models.TextField(null=False, verbose_name="Содержание")
    datead = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Биография"
        verbose_name_plural = "Биография"
        db_table = 'biography_biography'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content
