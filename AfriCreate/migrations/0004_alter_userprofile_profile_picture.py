# Generated by Django 5.1.3 on 2024-11-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AfriCreate', '0003_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='https://res.cloudinary.com/dqky44kl4/image/upload/v1732417617/x0xnry4m57a0mpoasps9.webp', upload_to='profile_pictures/'),
        ),
    ]
