# Generated by Django 5.0.6 on 2024-06-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0002_alter_artikel_options_alter_kategori_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='artikel'),
        ),
    ]
