from django.http import HttpResponse
from django.views.generic import TemplateView
from accounts.models import User
from blogs.models import Article


class Index(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.filter(is_highlighted=True).first()
        context['articles'] = Article.objects.filter(is_highlighted=False).exclude(tags__name__in=['Trabalhos Realizados']).order_by('-created_at')[:4]
        context['article_academic'] = Article.objects.filter(tags__name__in=['Acadêmico'])
        articles = Article.objects.filter(tags__name__in=['Trabalhos Realizados'])
        articles_per_list = 2
        context['article_jobs'] = [list(articles[i:i + articles_per_list]) for i in range(0, len(articles), articles_per_list)]

        return context


def robots_txt(request):
    content = ("User-agent: *\n"
               "Allow: /\n"
               "Disallow: /admin/\n")
    return HttpResponse(content, content_type="text/plain")
