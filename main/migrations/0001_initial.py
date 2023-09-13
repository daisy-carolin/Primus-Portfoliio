# Generated by Django 4.2.5 on 2023-09-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UploadedFile",
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
                ("file", models.FileField(upload_to="static/images")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]