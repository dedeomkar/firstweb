# Generated by Django 2.0.7 on 2019-03-06 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='featu',
            field=models.CharField(choices=[('a', 'average'), ('b', 'better'), ('g', 'good'), ('bs', 'best')], default='a', max_length=55),
        ),
    ]
