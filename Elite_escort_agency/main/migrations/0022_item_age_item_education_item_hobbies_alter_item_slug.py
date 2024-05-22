# Generated by Django 5.0.1 on 2024-05-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_reviews_options_remove_item_instructions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='education',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='item',
            name='hobbies',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='girls'),
        ),
    ]