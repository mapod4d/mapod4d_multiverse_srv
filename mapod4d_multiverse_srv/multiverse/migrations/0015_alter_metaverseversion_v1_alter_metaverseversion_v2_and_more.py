# Generated by Django 4.1.5 on 2023-04-22 02:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiverse', '0014_metaverseversion_p_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metaverseversion',
            name='v1',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='metaverseversion',
            name='v2',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='metaverseversion',
            name='v3',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='metaverseversion',
            name='v4',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
    ]