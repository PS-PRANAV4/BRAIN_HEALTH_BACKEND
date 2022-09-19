# Generated by Django 4.1 on 2022-09-12 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_alter_comments_post_alter_comments_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='group_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='groups',
            name='group_profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='group/group_profile_pic'),
        ),
    ]
