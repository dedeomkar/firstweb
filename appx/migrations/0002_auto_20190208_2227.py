# Generated by Django 2.0.7 on 2019-02-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lsd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.TextField()),
                ('a2', models.TextField()),
                ('a3', models.TextField(default='hey.. lol')),
            ],
        ),
        migrations.DeleteModel(
            name='lists',
        ),
    ]
