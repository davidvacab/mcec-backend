# Generated by Django 4.2.4 on 2023-08-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_profile_voice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='members/default.jpg', upload_to='members/profile_pics/', verbose_name='profile picture'),
        ),
    ]
