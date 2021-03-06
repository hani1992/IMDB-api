# Generated by Django 3.1.4 on 2020-12-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('yearCreated', models.IntegerField()),
                ('rate', models.FloatField()),
                ('poster', models.TextField()),
                ('trailer', models.TextField()),
                ('tag', models.ManyToManyField(to='api.Tag')),
            ],
        ),
    ]
