# Generated by Django 3.1.3 on 2020-12-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201216_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='name',
            field=models.CharField(choices=[('M', 'Mubaarak'), ('N', 'Nabeel'), ('AM', 'Abdul-Mujeeb')], max_length=50),
        ),
    ]