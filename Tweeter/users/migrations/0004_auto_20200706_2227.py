# Generated by Django 3.0.7 on 2020-07-06 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200706_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='message',
            field=models.CharField(max_length=250),
        ),
    ]
