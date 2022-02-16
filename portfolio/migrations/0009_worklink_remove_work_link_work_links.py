# Generated by Django 4.0.1 on 2022-02-16 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_work_subgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('link', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='work',
            name='link',
        ),
        migrations.AddField(
            model_name='work',
            name='links',
            field=models.ManyToManyField(to='portfolio.WorkLink'),
        ),
    ]