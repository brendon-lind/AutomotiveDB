# Generated by Django 3.0.5 on 2020-05-24 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='portrait',
            field=models.ImageField(default='user_silhouette.png', upload_to=''),
        ),
    ]
