# Generated by Django 4.0.4 on 2022-04-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posteos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=3000)),
            ],
            options={
                'verbose_name': 'posteo',
                'verbose_name_plural': 'posteos',
            },
        ),
    ]