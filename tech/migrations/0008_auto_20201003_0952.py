# Generated by Django 2.0 on 2020-10-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0007_emailnotconform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailnotconform',
            old_name='email',
            new_name='noemail',
        ),
        migrations.RenameField(
            model_name='emailnotconform',
            old_name='role',
            new_name='norole',
        ),
    ]
