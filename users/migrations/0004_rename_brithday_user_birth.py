# Generated by Django 4.0.4 on 2022-05-26 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='brithday',
            new_name='birth',
        ),
    ]
