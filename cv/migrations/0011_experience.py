# Generated by Django 4.0.1 on 2022-02-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_remove_education_years_education_end_education_start_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(default='Company', max_length=128)),
                ('position', models.CharField(default='Position', max_length=128)),
                ('description', models.CharField(default='description here. Lorem Ipsum sig dol loriet', max_length=1024)),
                ('start', models.CharField(default='1995', max_length=128)),
                ('end', models.CharField(default='2100', max_length=128)),
            ],
        ),
    ]