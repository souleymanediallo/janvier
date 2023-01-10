from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('new/', views.ArticleCreateView.as_view(), name='article-create'),
    path('all-categories/', views.all_categories, name='all-categories'),
    path('all-subcategories/', views.all_subcategories, name='all-subcategories'),
]