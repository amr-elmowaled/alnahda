# Generated by Django 2.1.1 on 2019-05-24 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190524_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='subject',
            new_name='subjects',
        ),
    ]
