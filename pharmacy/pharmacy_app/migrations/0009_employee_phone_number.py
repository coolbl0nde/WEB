# Generated by Django 4.2.1 on 2023-09-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_app', '0008_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
