# Generated by Django 3.2 on 2021-09-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eagro', '0002_alter_signupuser_sdob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='signupuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='signupuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
