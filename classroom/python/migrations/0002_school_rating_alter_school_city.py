# Generated by Django 4.1.3 on 2022-11-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
