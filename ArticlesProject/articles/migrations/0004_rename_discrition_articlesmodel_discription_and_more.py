# Generated by Django 4.2 on 2023-11-16 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articlesmodel_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlesmodel',
            old_name='discrition',
            new_name='discription',
        ),
        migrations.AlterField(
            model_name='articlesmodel',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 11, 16, 20, 55, 17, 902838, tzinfo=datetime.timezone.utc)),
        ),
    ]
