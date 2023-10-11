from django.shortcuts import render, HttpResponse
from .models import Article, Category

# Create your views here.

def home_view(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, 'web_site/index.html', context)


def category_articles(request, category_id):
    category = Category.objects.get(pk=category_id)
    articles = category.articles.all()
    context = {
        "articles": articles
    }
    return render(request, 'web_site/index.html', context)

