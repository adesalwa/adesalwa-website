# Generated by Django 3.2.8 on 2021-11-22 06:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_artikel_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
