# Generated by Django 4.0.4 on 2022-06-27 11:14

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rightnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='rightnews',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='rightnews',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
