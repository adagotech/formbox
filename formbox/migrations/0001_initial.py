# Generated by Django 5.0.1 on 2024-01-09 03:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('protection', models.CharField(choices=[('NONE', 'None'), ('HCAPTCHA', 'hCaptcha'), ('RECAPTCHA', 'Re-Captcha')], max_length=10)),
                ('protection_key', models.CharField(max_length=255, null=True)),
                ('notification', models.CharField(choices=[('NONE', 'None'), ('IMMEDIATE', 'Immediate'), ('DIGEST', 'Digest')], max_length=10)),
                ('digest_time', models.IntegerField(null=True)),
                ('digest_day_part', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formbox.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.JSONField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formbox.project')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formbox.team'),
        ),
    ]
