# Generated by Django 3.2.9 on 2021-12-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_tweet_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.TextField(max_length=280),
        ),
    ]