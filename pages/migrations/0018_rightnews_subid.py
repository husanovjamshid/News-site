# Generated by Django 4.0.4 on 2022-07-15 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_rightnews_shorttext'),
    ]

    operations = [
        migrations.AddField(
            model_name='rightnews',
            name='subId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategory', to='pages.category'),
        ),
    ]
