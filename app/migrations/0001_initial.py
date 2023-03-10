# Generated by Django 4.1.4 on 2022-12-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=20, unique=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('company_name', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField(null=True)),
                ('date_of_leaving', models.DateField(null=True)),
                ('department', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(default='employee', max_length=100)),
            ],
        ),
    ]
