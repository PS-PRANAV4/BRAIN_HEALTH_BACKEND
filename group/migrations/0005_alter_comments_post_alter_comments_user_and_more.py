# Generated by Django 4.1 on 2022-09-07 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_alter_doccertificate_certi'),
        ('group', '0004_alter_groups_group_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='group.post'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='groups',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='accounts.doccertificate'),
        ),
        migrations.AlterField(
            model_name='post',
            name='groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='group.groups'),
        ),
    ]
