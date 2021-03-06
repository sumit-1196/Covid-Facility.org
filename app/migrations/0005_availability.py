# Generated by Django 3.2 on 2021-05-18 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='app.hospital')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='app.service')),
            ],
        ),
    ]
