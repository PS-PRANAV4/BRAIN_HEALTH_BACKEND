# Generated by Django 4.1 on 2022-09-06 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_doccertificate_certi'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.post'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doccertificate'),
        ),
    ]
