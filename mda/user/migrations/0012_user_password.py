# Generated by Django 2.0.3 on 2018-04-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=155),
            preserve_default=False,
        ),
    ]
