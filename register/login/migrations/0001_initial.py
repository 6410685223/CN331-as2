# Generated by Django 4.2.5 on 2023-09-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=5)),
                ('surname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
            ],
        ),
    ]
