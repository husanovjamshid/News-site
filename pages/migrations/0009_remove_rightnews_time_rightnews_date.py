# Generated by Django 4.0.4 on 2022-06-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_remove_rightnews_date_rightnews_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rightnews',
            name='time',
        ),
        migrations.AddField(
            model_name='rightnews',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
