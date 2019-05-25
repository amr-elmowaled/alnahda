# Generated by Django 2.1.1 on 2019-05-25 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190525_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
            preserve_default=False,
        ),
    ]
