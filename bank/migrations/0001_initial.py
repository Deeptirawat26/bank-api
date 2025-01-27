# Generated by Django 5.1 on 2024-09-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('name', models.CharField(max_length=49)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('bank_id', models.BigIntegerField()),
                ('branch', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank_name', models.CharField(max_length=49)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('ifsc',), name='unique_ifsc')],
            },
        ),
    ]
