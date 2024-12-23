# Generated by Django 5.1.3 on 2024-11-25 09:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_customuser_email_alter_customuser_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencerprofile',
            name='post_id',
            field=models.ForeignKey(db_column='post_id', default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
