# Generated by Django 3.1.4 on 2020-12-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='test',
            field=models.FloatField(null=True),
        ),
    ]
