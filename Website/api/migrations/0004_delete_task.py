# Generated by Django 3.2.12 on 2022-02-20 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_task_gender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
