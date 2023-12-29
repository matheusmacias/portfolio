from django.urls import path
from .views import Index, robots_txt

app_name = 'main'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('robots.txt', robots_txt, name='robots_txt'),
]
