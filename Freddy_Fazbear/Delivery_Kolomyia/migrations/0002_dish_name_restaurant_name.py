# Generated by Django 4.2.6 on 2023-10-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery_Kolomyia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='name',
            field=models.CharField(default='Default Name', max_length=30),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='name',
            field=models.CharField(default='Default Name', max_length=30),
        ),
    ]
