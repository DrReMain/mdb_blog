from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, 'index.html')

def homepage(request):

	return render(request, 'home_page.html')