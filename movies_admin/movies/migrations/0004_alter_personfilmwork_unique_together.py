# Generated by Django 3.2 on 2022-08-17 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20220817_1640'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personfilmwork',
            unique_together={('film_work_id', 'person_id')},
        ),
    ]
