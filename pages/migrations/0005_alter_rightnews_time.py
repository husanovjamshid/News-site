# Generated by Django 4.0.4 on 2022-06-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_rightnews_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rightnews',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
