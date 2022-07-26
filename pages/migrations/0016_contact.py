# Generated by Django 4.0.4 on 2022-07-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_centernews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('message', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
