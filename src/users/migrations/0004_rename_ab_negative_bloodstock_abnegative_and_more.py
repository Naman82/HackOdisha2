# Generated by Django 4.1.1 on 2022-09-10 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_bloodbank_bloodbankprofile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloodstock',
            old_name='AB_negative',
            new_name='abnegative',
        ),
        migrations.RenameField(
            model_name='bloodstock',
            old_name='AB_postive',
            new_name='abpostive',
        ),
        migrations.RenameField(
            model_name='bloodstock',
            old_name='A_negative',
            new_name='anegative',
        ),
        migrations.RenameField(
            model_name='bloodstock',
            old_name='A_postive',
            new_name='apostive',
        ),
        migrations.RenameField(
            model_name='bloodstock',
            old_name='B_negative',
            new_name='bnegative',
        ),
        migrations.RenameField(
            model_name='bloodstock',
            old_name='B_postive',
            new_name='bpostive',
        ),
        migrations.RenameField(
            model_name='bloodstock',
            old_name='O_negative',
            new_name='onegative',
        ),
        migrations.RenameField(
            model_name='bloodstock',
            old_name='O_postive',
            new_name='opostive',
        ),
        migrations.AlterField(
            model_name='bloodstock',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
