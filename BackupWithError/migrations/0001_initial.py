# Generated by Django 4.2.5 on 2023-09-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackupWithError',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('backup_id', models.CharField(max_length=100)),
                ('error_message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
