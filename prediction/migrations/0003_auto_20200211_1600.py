# Generated by Django 2.2.6 on 2020-02-11 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_predictionmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictionmodel',
            old_name='apt',
            new_name='aptitude',
        ),
        migrations.RenameField(
            model_name='predictionmodel',
            old_name='sie',
            new_name='technical',
        ),
    ]
