# Generated by Django 3.2 on 2022-08-17 13:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='creation_date')),
                ('rating', models.FloatField(default=0, verbose_name='rating')),
                ('type', models.CharField(choices=[('movie', 'Freshman'), ('tv_show', 'Sophomore')], default='movie', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Кинопроизведения',
                'verbose_name_plural': 'Кинопроизведения',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'content"."genre',
            },
        ),
    ]