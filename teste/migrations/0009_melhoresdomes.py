# Generated by Django 2.0.3 on 2018-03-29 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0008_auto_20180329_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='MelhoresDoMes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=4)),
                ('vendasMes', models.CharField(max_length=100)),
            ],
        ),
    ]
