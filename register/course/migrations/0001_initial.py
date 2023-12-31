# Generated by Django 4.2.5 on 2023-10-06 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('course_term', models.CharField(choices=[('1', '1'), ('2', '2'), ('Summer', 'Summer')], default='1', max_length=6)),
                ('course_year', models.IntegerField(choices=[(2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032)], default=2023)),
                ('avilable_seat', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('course_is_open', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='class_of_students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=30)),
                ('student_lastname', models.CharField(max_length=30)),
                ('course', models.ManyToManyField(to='course.course')),
            ],
        ),
    ]
