from django.shortcuts import render, HttpResponseRedirect


# Create your views here.

def main(request):
    return HttpResponseRedirect('/index')


def index(request):
    return render(request, 'index.html')


def homepage(request):
    url = request.path

    return render(request, 'home_page.html', locals())


def postpage(request):
    url = request.path
    return render(request, 'post_page.html', locals())
