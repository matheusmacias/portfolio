import os
import uuid

from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Tag(models.Model):
    name = models.CharField("Nome", max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(max_length=255)
    original_headline = models.CharField(max_length=255, editable=False, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, editable=False, null=False, blank=False)
    image = models.ImageField(upload_to='article/images/', blank=True, null=True)
    authors = models.ManyToManyField(User, related_name='news_articles')
    content = CKEditor5Field("Texto", config_name="extends")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="articles", verbose_name="Tags", blank=True)
    is_highlighted = models.BooleanField('Destaque', default=False)

    def save(self, *args, **kwargs):
        if not self.original_headline:
            self.original_headline = self.headline

        if not self.slug:
            base_slug = slugify(self.headline)
            self.slug = f"{base_slug}-{str(uuid.uuid4().hex)[:4]}"
            self.slug = self.slug.lower()

        if self.headline != self.original_headline:
            base_slug = slugify(self.headline)
            self.slug = f"{base_slug}-{str(uuid.uuid4().hex)[:4]}"
            self.slug = self.slug.lower()
            self.original_headline = self.headline

        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.headline


@receiver(models.signals.pre_delete, sender=Article)
def auto_delete_files_article(sender, instance, **kwargs):
    if instance.image:
        os.remove(instance.image.path)
