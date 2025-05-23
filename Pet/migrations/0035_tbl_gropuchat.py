# Generated by Django 5.2 on 2025-04-16 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_delete_tbl_doctor'),
        ('Pet', '0034_tbl_chat_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_gropuchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_content', models.CharField(max_length=500)),
                ('chat_time', models.DateTimeField()),
                ('chat_file', models.FileField(upload_to='ChatFiles/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pet.tbl_post')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_pet')),
            ],
        ),
    ]
