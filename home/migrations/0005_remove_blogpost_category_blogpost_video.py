# Generated by Django 5.2 on 2025-05-07 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blogpost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='category',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='blog_videos/'),
        ),
    ]
