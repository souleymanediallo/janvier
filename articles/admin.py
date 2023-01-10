from django.contrib import admin
from .models import Article, Category, ImageArticle, SubCategory, Tag, Condition, Color, MainCategory, Size
# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(ImageArticle)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Condition)
admin.site.register(Color)
admin.site.register(MainCategory)
admin.site.register(Size)

# Compare this snippet from articles/forms.py:
# from django import forms
