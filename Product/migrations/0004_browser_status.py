# Generated by Django 2.1.11 on 2020-05-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20200525_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='browser',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
