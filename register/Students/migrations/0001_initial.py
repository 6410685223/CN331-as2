# Generated by Django 4.2.5 on 2023-10-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_class',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('student_surname', models.CharField(max_length=30)),
                ('student_lasname', models.CharField(max_length=30)),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('student_username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('student_password', models.CharField(max_length=30)),
                ('student_surname', models.CharField(max_length=30)),
                ('student_lasname', models.CharField(max_length=30)),
            ],
        ),
    ]
