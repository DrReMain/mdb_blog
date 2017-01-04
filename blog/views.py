# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from blog.models import *


# Create your views here.

def main(request):

    return HttpResponseRedirect('/index')


def index(request):

    return render(request, 'index.html')


def homepage(request):
    # 获取路径
    url = request.path

    # 查询父，子分类数据
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

    # 查询文章
    def article_scope():
        if article_scope_key == None:
            # 返回无分类的文章列表
            return Article.objects.all()
        else:
            # 通过分类值在子分类表里找到对应的id
            cate_index = CategoryChild.objects.get(name=article_scope_key).id
            # 返回对应分类的全部文章
            return Article.objects.filter(category_child_id=cate_index)

    article_list = article_scope()

    # 文章初级搜索功能
    key_word = request.GET.get('searchwords')
    if key_word != None:
        article_list = []
        for article in Article.objects.all():
            if key_word in article.desc or key_word in article.content or key_word in article.title:
                article_list.append(article)
    return render(request, 'home_page.html', locals())


def postpage(request, id):
    url = request.path
    CategoryParent_data = CategoryParent.objects.all()
    CategoryChild_data = CategoryChild.objects.all()
    article = Article.objects.get(id=id)

    return render(request, 'post_page.html', locals())
