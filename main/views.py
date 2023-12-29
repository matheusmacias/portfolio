from django.http import HttpResponse
from django.views.generic import TemplateView
from accounts.models import User, Experience
from blogs.models import Article


class Index(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = User.objects.filter(is_owner=True).first()
        context['experiences'] = Experience.objects.filter(user=context['owner']).order_by('-is_current', '-start_date')
        context['article'] = Article.objects.filter(is_highlighted=True).first()
        context['articles'] = Article.objects.filter(is_highlighted=False).order_by('-created_at')[:4]
        return context


def robots_txt(request):
    content = ("User-agent: *\n"
               "Allow: /\n"
               "Disallow: /admin/\n")
    return HttpResponse(content, content_type="text/plain")
