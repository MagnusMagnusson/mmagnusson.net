# Generated by Django 4.0.1 on 2022-01-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_rename_name_baseinfo_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseinfo',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
