# Generated by Django 2.1.15 on 2022-01-08 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingregients',
            new_name='ingredients',
        ),
    ]
