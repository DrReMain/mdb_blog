from django.shortcuts import render, HttpResponseRedirect
from blog.models import *


# Create your views here.

def main(request):
	return HttpResponseRedirect('/index')


def index(request):
	return render(request, 'index.html')


def homepage(request):
	url = request.path

	category_list = Category.objects.all()

	article_list = Article.objects.all()



	return render(request, 'home_page.html', locals())


def postpage(request, id):
	url = request.path

	category_list = Category.objects.all()

	index = id

	return render(request, 'post_page.html', locals())
