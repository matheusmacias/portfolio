from django.urls import path, include
from .views import Index, robots_txt
from blogs.views import ArticleWorkListView, ArticleWorkDetailView

app_name = 'main'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('trabalhos/', include([
        path('', ArticleWorkListView.as_view(), name='article_work_list'),
        path('<slug:slug>/', ArticleWorkDetailView.as_view(), name='article_work_detail'),
    ])),
]
