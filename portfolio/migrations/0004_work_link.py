# Generated by Django 4.0.1 on 2022-02-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_description_group_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
