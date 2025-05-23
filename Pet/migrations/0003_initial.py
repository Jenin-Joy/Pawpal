# Generated by Django 5.1.5 on 2025-03-12 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0005_delete_tbl_doctor'),
        ('Pet', '0002_delete_tbl_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_photo', models.FileField(upload_to='Assets/File/user')),
                ('post_description', models.CharField(max_length=30)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_pet')),
            ],
        ),
    ]
