# Generated by Django 3.0.3 on 2020-05-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_equities'),
    ]

    operations = [
        migrations.CreateModel(
            name='eqnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, null=True)),
                ('imgurl', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]