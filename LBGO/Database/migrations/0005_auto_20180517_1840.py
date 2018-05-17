# Generated by Django 2.0.2 on 2018-05-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0004_auto_20180517_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='questions',
            field=models.ManyToManyField(related_name='questions', to='Database.Question'),
        ),
        migrations.AlterField(
            model_name='team',
            name='visitedObjectives',
            field=models.ManyToManyField(related_name='visitedObjectives', to='Database.Objective'),
        ),
    ]