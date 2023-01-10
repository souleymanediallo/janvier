from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Category, SubCategory
from .forms import ArticleForm
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created']


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    context_object_name = 'form'
    success_message = "Votre article a été crée !"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def all_categories(request):
    main_categories = request.GET.get('main_category')
    categories = Category.objects.filter(main_category=main_categories)
    context = {'categories': categories}
    return render(request, 'partials/categories.html', context)


def all_subcategories(request):
    sub_categories = request.GET.get('sub_category')
    subcategories = SubCategory.objects.filter(category=sub_categories)
    context = {'subcategories': subcategories}
    return render(request, 'partials/sub-categories.html', context)
