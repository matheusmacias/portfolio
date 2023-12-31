from django.views.generic import DetailView, ListView
from accounts.models import User
from blogs.models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'details.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.all().exclude(tags__name__in=['Trabalhos Realizados']).order_by('-created_at')


class ArticleListView(ListView):
    model = Article
    template_name = 'list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().exclude(tags__name__in=['Trabalhos Realizados']).order_by('-created_at')


class ArticleWorkListView(ListView):
    model = Article
    template_name = 'jobs-list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().filter(tags__name__in=['Trabalhos Realizados']).order_by('-created_at')


class ArticleWorkDetailView(DetailView):
    model = Article
    template_name = 'details.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.all().filter(tags__name__in=['Trabalhos Realizados']).order_by('-created_at')