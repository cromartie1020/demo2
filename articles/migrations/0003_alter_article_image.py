# Generated by Django 3.2.5 on 2021-07-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='media'),
        ),
    ]
