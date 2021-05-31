# Generated by Django 3.2.3 on 2021-05-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('ISBN', models.TextField()),
                ('price', models.TextField()),
                ('published_year', models.TextField()),
                ('original_title', models.TextField()),
                ('language', models.TextField()),
                ('rating', models.TextField()),
                ('image_url', models.TextField()),
            ],
        ),
    ]