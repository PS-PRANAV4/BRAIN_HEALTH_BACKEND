# Generated by Django 4.1 on 2022-09-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icons', models.ImageField(blank=True, null=True, upload_to='photos/icon')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
