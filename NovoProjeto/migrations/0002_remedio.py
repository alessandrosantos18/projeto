# Generated by Django 2.2.3 on 2019-11-21 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovoProjeto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=255)),
            ],
        ),
    ]
