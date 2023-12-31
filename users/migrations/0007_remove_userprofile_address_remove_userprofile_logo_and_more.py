# Generated by Django 4.2.1 on 2023-09-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_remove_userprofile_picture_userprofile_logo_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="address",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="logo",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="ntn",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="parent_user",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="registration_no",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="social_links",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="strn",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="terms",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="title",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="active_flag",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="active_key",
            field=models.CharField(default=123, max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprofile",
            name="mac_address",
            field=models.CharField(default=1234, max_length=50),
            preserve_default=False,
        ),
    ]
