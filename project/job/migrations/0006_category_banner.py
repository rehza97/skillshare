# Generated by Django 5.0.2 on 2024-03-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_reviewrating_created_at_alter_reviewrating_ip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='category/banners/'),
        ),
    ]
