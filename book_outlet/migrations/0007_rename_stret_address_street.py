# Generated by Django 4.2.2 on 2023-07-05 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address_author_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='stret',
            new_name='street',
        ),
    ]
