from django.contrib import admin
from .models import Article
from .models import Lekcja
from .models import Category

admin.site.register(Article)
admin.site.register(Lekcja)
admin.site.register(Category)

