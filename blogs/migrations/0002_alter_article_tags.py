# Generated by Django 5.0 on 2023-12-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='blogs.tag', verbose_name='Tags'),
        ),
    ]
