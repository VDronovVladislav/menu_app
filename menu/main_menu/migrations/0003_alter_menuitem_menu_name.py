# Generated by Django 5.1.1 on 2024-09-27 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0002_menuitem_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='menu_name',
            field=models.CharField(default='main_menu', max_length=100, null=True),
        ),
    ]
