# Generated by Django 4.2.3 on 2023-07-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="is_reviewer",),
        migrations.RemoveField(model_name="userprofile", name="is_translator",),
        migrations.AddField(
            model_name="userprofile",
            name="role",
            field=models.CharField(
                choices=[
                    ("", ""),
                    ("is_translator", "Translator"),
                    ("is_reviewer", "Reviewer"),
                ],
                default=("", ""),
                max_length=100,
            ),
        ),
    ]