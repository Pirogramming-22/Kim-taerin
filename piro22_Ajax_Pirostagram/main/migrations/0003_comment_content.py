# Generated by Django 5.1.4 on 2025-01-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment_content_alter_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
