# Generated by Django 3.0.1 on 2020-01-02 09:37

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=blog.models.user_directory_path),
        ),
    ]
