# Generated by Django 3.0.2 on 2020-02-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFR1', '0035_delete_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video', models.FileField(upload_to='')),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
