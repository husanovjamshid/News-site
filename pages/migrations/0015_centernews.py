# Generated by Django 4.0.4 on 2022-06-30 13:10

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_rightnews_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('view_count', models.IntegerField(default=0, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.category')),
            ],
        ),
    ]
