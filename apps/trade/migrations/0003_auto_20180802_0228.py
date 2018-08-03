# Generated by Django 2.0.3 on 2018-08-02 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_paymentlogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentlogs',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='paymentlogs',
            name='object_id',
        ),
        migrations.AddField(
            model_name='paymentlogs',
            name='goods_sn',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='商品序列号'),
            preserve_default=False,
        ),
    ]
