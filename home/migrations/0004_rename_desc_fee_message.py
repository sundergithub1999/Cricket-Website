# Generated by Django 4.0 on 2022-01-25 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_emailid_fee_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='desc',
            new_name='message',
        ),
    ]
