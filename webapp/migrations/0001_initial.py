# Generated by Django 4.1.1 on 2022-09-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ic', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('POSITIVE', 'Positive'), ('NEGATIVE', 'Negative')], max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('street_address', models.CharField(max_length=40)),
                ('postcode', models.IntegerField()),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
            ],
        ),
    ]
