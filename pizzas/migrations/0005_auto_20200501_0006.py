# Generated by Django 3.0.5 on 2020-05-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_auto_20200430_2351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={},
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]