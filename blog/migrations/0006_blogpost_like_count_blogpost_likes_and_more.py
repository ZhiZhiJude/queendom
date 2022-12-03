# Generated by Django 4.1.2 on 2022-11-21 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_remove_blogpost_images_image_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='like_count',
            field=models.BigIntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='blogpost',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost'),
            preserve_default=False,
        ),
    ]