# Generated by Django 3.0.2 on 2024-07-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('bmi', models.FloatField()),
                ('children', models.FloatField()),
                ('sex_male', models.FloatField()),
                ('smoker_yes', models.FloatField()),
            ],
        ),
    ]
