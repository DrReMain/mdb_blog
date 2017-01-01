from django.conf.urls import url
from blog import views

urlpatterns = [

	url(r'^$', views.main),

	url(r'^index$', views.index, name="index"),

	url(r'^home$', views.homepage, name="homepage"),

	url(r'^post/(?P<id>\d+)$', views.postpage, name="postpage")

]