# Generated by Django 2.0.3 on 2018-08-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsorder',
            name='pay_time',
            field=models.DateTimeField(verbose_name='支付时间'),
        ),
        migrations.AlterField(
            model_name='goodsorder',
            name='sign_time',
            field=models.DateTimeField(verbose_name='签收时间'),
        ),
    ]
