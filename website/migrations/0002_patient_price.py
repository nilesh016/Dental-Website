# Generated by Django 3.1.7 on 2021-05-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
