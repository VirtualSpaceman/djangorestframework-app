# Generated by Django 2.0.3 on 2018-03-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0006_delete_maisvendidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaisVendidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=50)),
                ('qtd', models.IntegerField()),
            ],
        ),
    ]