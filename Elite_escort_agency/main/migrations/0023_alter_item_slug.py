# Generated by Django 5.0.1 on 2024-05-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_item_age_item_education_item_hobbies_alter_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='girl'),
        ),
    ]
