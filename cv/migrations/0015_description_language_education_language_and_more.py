# Generated by Django 4.0.1 on 2022-02-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0014_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='language',
            field=models.CharField(default='IS', max_length=2),
        ),
        migrations.AddField(
            model_name='education',
            name='language',
            field=models.CharField(default='IS', max_length=2),
        ),
        migrations.AddField(
            model_name='experience',
            name='language',
            field=models.CharField(default='IS', max_length=2),
        ),
        migrations.AddField(
            model_name='interest',
            name='language',
            field=models.CharField(default='IS', max_length=2),
        ),
        migrations.AddField(
            model_name='references',
            name='language',
            field=models.CharField(default='IS', max_length=2),
        ),
    ]
