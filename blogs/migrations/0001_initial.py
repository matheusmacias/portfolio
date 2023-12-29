# Generated by Django 5.0 on 2023-12-29 05:39

import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('original_headline', models.CharField(editable=False, max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='article/images/')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_highlighted', models.BooleanField(default=False, verbose_name='Destaque')),
                ('authors', models.ManyToManyField(related_name='news_articles', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, null=True, related_name='articles', to='blogs.tag', verbose_name='Tags')),
            ],
        ),
    ]
