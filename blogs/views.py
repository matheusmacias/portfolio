from django.views.generic import DetailView, ListView
from accounts.models import User
from blogs.models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'details.html'
    context_object_name = 'article'


class ArticleListView(ListView):
    model = Article
    template_name = 'list.html'
    context_object_name = 'articles'
