# Generated by Django 5.0.4 on 2024-04-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=126, null=True, verbose_name='密码'),
        ),
    ]
