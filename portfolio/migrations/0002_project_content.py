# Generated by Django 4.0.6 on 2022-07-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
