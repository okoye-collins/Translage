# Generated by Django 4.2.3 on 2023-09-11 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="documents/files")),
            ],
        ),
        migrations.CreateModel(
            name="SentenceTokenize",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task", models.CharField(max_length=300)),
                (
                    "file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="translator.file",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Translation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("english", "english"),
                            ("Igbo", "Igbo"),
                            ("Yoruba", "Yoruba"),
                            ("Hausa", "Hausa"),
                        ],
                        default="english",
                        max_length=100,
                    ),
                ),
                ("translation", models.TextField()),
                (
                    "totranslate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="translator.sentencetokenize",
                    ),
                ),
                (
                    "translator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.userprofile",
                    ),
                ),
            ],
        ),
    ]
