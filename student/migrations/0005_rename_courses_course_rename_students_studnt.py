# Generated by Django 5.1.1 on 2024-11-17 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_courses_department_students_delete_studnt_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='courses',
            new_name='course',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Studnt',
        ),
    ]