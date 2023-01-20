from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle
from django.views.generic import UpdateView, DeleteView,ListView


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'slug', 'body', 'image', 'author']

class ArticleDeleteView(DeleteView):
    model = Article
    success_url=reverse_lazy('list')

'''
@login_required(login_url='/accounts/login')
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})
'''

class ArticleListView(ListView):
    paginate_by = 6
    model = Article

def article_detail(request, id):

    article = Article.objects.get(id=id)

    return render(request, 'articles/detail.html', {'article': article})







@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('list')

    else:
        form = CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


