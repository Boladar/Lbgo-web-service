# Generated by Django 2.0.2 on 2018-05-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='endTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
