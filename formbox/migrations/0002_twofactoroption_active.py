# Generated by Django 5.0.1 on 2024-01-20 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twofactoroption',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
