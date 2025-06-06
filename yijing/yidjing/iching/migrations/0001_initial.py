# Generated by Django 5.1.2 on 2025-03-04 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hexagram",
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
                ("number", models.PositiveIntegerField(unique=True)),
                ("chinese_name", models.CharField(max_length=20)),
                ("pinyin", models.CharField(blank=True, max_length=20)),
                (
                    "binary",
                    models.CharField(
                        help_text="Binary representation of the hexagram",
                        max_length=6,
                        unique=True,
                    ),
                ),
                ("judgment_zh", models.TextField(help_text="Judgment in Chinese")),
                (
                    "judgment_en",
                    models.TextField(blank=True, help_text="Judgment in English"),
                ),
                (
                    "judgment_es",
                    models.TextField(blank=True, help_text="Judgment in Spanish"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Consultation",
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
                    "compact_representation",
                    models.CharField(
                        help_text="Compact representation of the consultation, e.g., 678967",
                        max_length=6,
                    ),
                ),
                (
                    "changing_hexagram",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consultations_as_transformed",
                        to="iching.hexagram",
                    ),
                ),
                (
                    "primary_hexagram",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consultations_as_primary",
                        to="iching.hexagram",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Line",
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
                    "line_number",
                    models.PositiveIntegerField(
                        help_text="Line number, e.g., 1 for 初九"
                    ),
                ),
                (
                    "text_zh",
                    models.TextField(help_text="Original Chinese text for the line"),
                ),
                (
                    "text_en",
                    models.TextField(
                        blank=True, help_text="English translation for the line"
                    ),
                ),
                (
                    "text_es",
                    models.TextField(
                        blank=True, help_text="Spanish translation for the line"
                    ),
                ),
                (
                    "hexagram",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lines",
                        to="iching.hexagram",
                    ),
                ),
            ],
            options={
                "unique_together": {("hexagram", "line_number")},
            },
        ),
    ]
