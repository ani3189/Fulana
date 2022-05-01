# Generated by Django 4.0.4 on 2022-04-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFulana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='institutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituto', models.CharField(max_length=30)),
                ('review', models.TextField()),
            ],
            options={
                'verbose_name': 'instituto',
                'verbose_name_plural': 'institutos',
            },
        ),
        migrations.CreateModel(
            name='lenguaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenguaje', models.CharField(max_length=30)),
                ('review', models.TextField()),
            ],
            options={
                'verbose_name': 'lenguaje',
                'verbose_name_plural': 'lenguajes',
            },
        ),
        migrations.AlterField(
            model_name='posteos',
            name='post',
            field=models.TextField(),
        ),
    ]
