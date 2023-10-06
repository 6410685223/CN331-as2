# Generated by Django 4.2.5 on 2023-09-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_info_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='info_students',
            fields=[
                ('student_username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('student_password', models.CharField(max_length=10)),
                ('student_surname', models.CharField(max_length=30)),
                ('student_lasname', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='info_student',
        ),
    ]