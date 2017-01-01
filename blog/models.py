from __future__ import unicode_literals

from django.db import models


# Create your models here.

class CategoryParent(models.Model):
	icon = models.CharField(max_length=40, null=True)
	name = models.CharField(max_length=40, null=True)


class CategoryChild(models.Model):
	name = models.CharField(max_length=40, null=True)
	category_parent = models.ForeignKey(CategoryParent)
