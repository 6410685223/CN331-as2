# Generated by Django 4.2.5 on 2023-09-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0010_alter_course_course_is_open'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('student_surname', models.CharField(max_length=30)),
                ('student_lasname', models.CharField(max_length=30)),
                ('course_name', models.ManyToManyField(to='course.course')),
            ],
        ),
    ]