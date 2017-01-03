# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('分类名称', max_length=40, null=True)
    level = models.IntegerField('级别', default=1)
    parent = models.CharField('父级分类', max_length=40, null=True)
    icon = models.CharField('分类图标（奥森字体class名， 例： fa-html5）', max_length=40)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=20, default='Dr.ReMain', verbose_name='作者名称')

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __unicode__(self):
        return self.name


class Article(models.Model):
    article_img = models.URLField(null=True)
    category_child = models.ForeignKey(Category, verbose_name='所属子分类')
    title = models.CharField(max_length=200, default='文章标题', verbose_name='文章标题')
    desc = models.TextField(max_length=500, null=True, verbose_name='文章描述')
    author = models.ForeignKey(Author, verbose_name='作者')
    publication_date = models.DateField(verbose_name='发表日期')
    content = models.TextField(max_length=10000, null=True, verbose_name='文章内容')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['publication_date', 'author', 'title', 'category_child']


    def __unicode__(self):
        return self.title
