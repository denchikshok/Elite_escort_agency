# Generated by Django 5.0.6 on 2024-05-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='boobs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='status',
            field=models.CharField(choices=[('В процессе', 'В процессе'), ('Выполнен', 'Выполнен')], default='В процессе', max_length=20),
        ),
    ]
