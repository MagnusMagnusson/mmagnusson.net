# Generated by Django 4.0.1 on 2022-02-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_alter_baseinfo_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('job', models.CharField(max_length=128)),
                ('relation', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=128)),
                ('phone', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
