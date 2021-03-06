# Generated by Django 3.1.5 on 2021-01-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='status',
            field=models.CharField(choices=[('yes', 'Subscribed User'), ('no', 'Guest User')], default=0, max_length=30, verbose_name='STATUS'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new',
            name='upload',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
