# Generated by Django 2.0.3 on 2018-03-29 00:22

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('vendedor', models.CharField(max_length=30)),
                ('clienteId', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='teste.Cliente')),
            ],
        ),
    ]
