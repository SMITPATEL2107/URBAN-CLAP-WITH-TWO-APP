# Generated by Django 2.0 on 2020-10-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0003_emailconform_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconform',
            name='role',
            field=models.CharField(max_length=50),
        ),
    ]
