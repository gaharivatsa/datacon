# Generated by Django 4.2.5 on 2023-09-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_remove_userprofile_full_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="datacon",
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
                ("title", models.TextField(blank=True)),
                ("subtitle", models.TextField(blank=True)),
                ("content", models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(model_name="userprofile", name="user",),
        migrations.DeleteModel(name="Note",),
        migrations.DeleteModel(name="UserProfile",),
    ]
