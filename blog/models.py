# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class CategoryParent(models.Model):
	icon = models.CharField(max_length=40, null=True, verbose_name='父分类图标（奥森字体class名， 例： fa-html5）')
	name = models.CharField(max_length=40, null=True, verbose_name='父分类名称')

	class Meta:
		verbose_name = '父分类'
		verbose_name_plural = '父分类'

	def __unicode__(self):
		return self.name


class CategoryChild(models.Model):
	name = models.CharField(max_length=40, null=True, verbose_name='子分类名称')
	category_parent = models.ForeignKey(CategoryParent, verbose_name='子分类所属')

	class Meta:
		verbose_name = '子分类'
		verbose_name_plural = '子分类'

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
	category_parent = models.ForeignKey(CategoryParent, verbose_name='所属父分类')
	category_child = models.ForeignKey(CategoryChild, verbose_name='所属子分类')
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
