# Generated by Django 2.0.6 on 2018-07-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]