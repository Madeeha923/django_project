# Generated by Django 5.1.1 on 2024-11-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_contact_studentid_contact_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('student_id', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
            ],
        ),
    ]
