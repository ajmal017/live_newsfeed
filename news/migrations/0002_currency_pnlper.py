# Generated by Django 3.0.3 on 2020-05-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='pnlper',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]