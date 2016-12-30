from django.conf.urls import url
from blog import views

urlpatterns = [

	url(r'^$', views.index, name="index"),

	url(r'^home$', views.homepage, name="homepage")

]