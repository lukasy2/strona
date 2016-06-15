from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Post
from artykuly.models import Article
from artykuly.models import Lekcja
from artykuly.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.db.models import Q


def post_list(request):
    posts = Post.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    artykuly = Article.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    kategorie = Category.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_list.html', {'posts': posts, 'artykuly': artykuly, 'kategorie': kategorie})
	
# @login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    czyobraz = Post.objects.filter(Q(docfile__endswith='png') | Q(docfile__endswith='jpg') | Q(docfile__endswith='bmp') | Q(docfile__endswith='gif') | Q(docfile__endswith='jpeg'))
    posts = Post.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_detail.html', {'post': post, 'posts': posts, 'czyobraz': czyobraz})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))
	
    args['form'] = UserCreationForm()
    return render_to_response('registration/register.html', args)

	
def register_success(request):
    return render_to_response('registration/register_success.html')

	
def article_list(request):
    articles = Article.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    lekcje = Lekcja.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    kategorie = Category.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_list.html', {'articles': articles, 'lekcje': lekcje, 'kategorie': kategorie})
	
# @login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    lessons = Lekcja.objects.filter(Q(data_opublikowania__lte=timezone.now()), Q(kurs__tytul__contains=article.tytul))
    czyobraz = Article.objects.filter(Q(docfile__endswith='png') | Q(docfile__endswith='jpg') | Q(docfile__endswith='bmp') | Q(docfile__endswith='gif') | Q(docfile__endswith='jpeg'))
    articles = Article.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_detail.html', {'article': article, 'articles': articles, 'czyobraz': czyobraz, 'lessons': lessons})
	
def lesson_list(request):
    lessons = Lekcja.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_list.html', {'lessons': lessons})
	
# @login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lekcja, pk=pk)
    czyobraz = Lekcja.objects.filter(Q(docfile__endswith='png') | Q(docfile__endswith='jpg') | Q(docfile__endswith='bmp') | Q(docfile__endswith='gif') | Q(docfile__endswith='jpeg'))
    lessons = Lekcja.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_detail.html', {'lesson': lesson, 'lessons': lessons, 'czyobraz': czyobraz})
	
def category_list(request):
    categories = Category.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    artykuly = Article.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_list.html', {'categories': categories, 'artykuly': artykuly})
	
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    articles = Article.objects.filter(Q(data_opublikowania__lte=timezone.now()), Q(kategoria__tytul__contains=category.tytul))
    categories = Category.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_detail.html', {'category': category, 'categories': categories, 'articles': articles})