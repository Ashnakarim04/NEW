# Generated by Django 4.2.4 on 2023-09-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_img_companyprofile_criteria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='criteria',
        ),
        migrations.AddField(
            model_name='jobs',
            name='criteria',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
