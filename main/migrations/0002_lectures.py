# Generated by Django 3.1.4 on 2021-04-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=200)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('notes', models.TextField(default='')),
            ],
        ),
    ]
