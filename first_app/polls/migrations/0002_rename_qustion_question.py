# Generated by Django 3.2.5 on 2021-07-21 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Qustion',
            new_name='Question',
        ),
    ]