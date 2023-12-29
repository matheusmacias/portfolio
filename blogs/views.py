from django.views.generic import DetailView, ListView
from accounts.models import User
from blogs.models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'details.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = User.objects.filter(is_owner=True).first()
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'list.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = User.objects.filter(is_owner=True).first()
        return context
