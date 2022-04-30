# Generated by Django 4.0 on 2022-04-30 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_name', models.CharField(default='NA', max_length=256)),
                ('gender', models.CharField(default='NA', max_length=10)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('phone_no', models.BigIntegerField(blank=True, max_length=10, null=True)),
                ('DR_preferred', models.CharField(default='NA', max_length=256)),
            ],
        ),
    ]