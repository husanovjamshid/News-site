# Generated by Django 4.0.4 on 2022-06-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rightnews_img_alter_rightnews_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rightnews',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]