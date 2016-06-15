from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Article

def article_list(request):
    articles = Article.objects.filter(data_opublikowania__lte=timezone.now()).order_by('data_opublikowania')
    return render(request, 'newsy/post_list.html', {'articles': articles})
	
# @login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'newsy/post_detail.html', {'article': article})

