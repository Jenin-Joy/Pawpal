# Generated by Django 5.1.5 on 2025-03-13 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0015_tbl_grp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_lostpet',
        ),
    ]
