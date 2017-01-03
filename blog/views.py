# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from blog.models import *


# Create your views here.

def main(request):
	return HttpResponseRedirect('/index')


def index(request):
	return render(request, 'index.html')


def homepage(request):
	url = request.path
	CategoryParent_data = CategoryParent.objects.all()
	CategoryChild_data = CategoryChild.objects.all()
	# 找到get请求的category(分类)值
	article_scope_key = request.GET.get('category')

	# 根据请求的分类名，取得分类描述
	def cate_desc():
		for item in CategoryChild_data:
			if item.name == article_scope_key:
				return item.category_desc

	cate_desc_content = cate_desc()

	def article_scope():
		if article_scope_key == None:
			# 如果没有请求分类，则返回完整的文章列表
			return Article.objects.all()
		else:
			# 通过分类值在子分类表里找到对应的id
			cate_index = CategoryChild.objects.get(name=article_scope_key).id
			# 返回对应id的文章列表
			return Article.objects.filter(category_child_id=cate_index)

	article_list = article_scope()

	return render(request, 'home_page.html', locals())


def postpage(request, id):
	url = request.path
	CategoryParent_data = CategoryParent.objects.all()
	CategoryChild_data = CategoryChild.objects.all()
	article = Article.objects.get(id=id)

	return render(request, 'post_page.html', locals())
