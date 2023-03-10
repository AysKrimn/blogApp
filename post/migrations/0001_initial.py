# Generated by Django 4.1.1 on 2023-01-25 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Post Başlığı')),
                ('endPoint', models.SlugField(default='', verbose_name='URL')),
                ('message', models.TextField(default='', max_length=350, verbose_name='Mesaj')),
                ('image', models.FileField(blank=True, null=True, upload_to='banner', verbose_name='Post Resmi')),
                ('createdAt', models.DateTimeField(auto_now=True, verbose_name='Oluşturulma Tarihi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Postu Oluşturan')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Mesaj')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yorum Yapan')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='post.post', verbose_name='Gönderi')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
