# Generated by Django 5.0 on 2023-12-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pessoa",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("apelido", models.CharField(max_length=32)),
                ("nome", models.CharField(max_length=100)),
                ("nascimento", models.DateField()),
                ("stacka", models.JSONField()),
            ],
        ),
    ]
