# Generated by Django 4.0.6 on 2022-07-23 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ichki',
            name='bolim',
            field=models.ForeignKey(auto_created='bolim_ichkilari', null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.bolim'),
        ),
    ]
