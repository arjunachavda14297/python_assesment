# Generated by Django 4.1.2 on 2023-02-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('mobile', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(upload_to='profile_pic/')),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
