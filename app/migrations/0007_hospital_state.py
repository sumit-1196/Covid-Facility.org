# Generated by Django 3.2 on 2021-05-20 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210518_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='state',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.state'),
        ),
    ]