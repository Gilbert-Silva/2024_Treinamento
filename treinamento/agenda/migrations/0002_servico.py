# Generated by Django 5.0.6 on 2024-05-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('duracao', models.IntegerField()),
            ],
        ),
    ]