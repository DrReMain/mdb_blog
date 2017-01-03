from django.contrib import admin
from blog.models import *

# Register your models here.


admin.site.register(Author)
admin.site.register(Article)
admin.site.register(CategoryChild)
admin.site.register(CategoryParent)