# Generated by Django 5.1.1 on 2024-11-17 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_rename_courses_course_rename_students_studnt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='c_name',
            new_name='name',
        ),
    ]
