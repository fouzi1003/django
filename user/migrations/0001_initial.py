# Generated by Django 2.2.1 on 2019-05-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_dob', models.DateField(auto_now_add=True)),
                ('user_age', models.IntegerField()),
                ('user_company', models.CharField(max_length=20)),
                ('user_designation', models.CharField(max_length=20)),
                ('user_phone', models.IntegerField()),
            ],
        ),
    ]
