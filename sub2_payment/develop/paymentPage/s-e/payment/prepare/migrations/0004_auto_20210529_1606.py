# Generated by Django 3.2.3 on 2021-05-29 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prepare', '0003_auto_20210529_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_author',
            new_name='book_price',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_title',
        ),
    ]
