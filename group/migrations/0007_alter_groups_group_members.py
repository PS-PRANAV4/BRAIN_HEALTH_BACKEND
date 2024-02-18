# Generated by Django 5.0.2 on 2024-02-17 15:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_groups_group_description_groups_group_profile_pic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='group_members',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_conections', to=settings.AUTH_USER_MODEL),
        ),
    ]