# Generated by Django 4.2 on 2025-03-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('emotion', models.CharField(max_length=10)),
                ('content', models.TextField()),
            ],
        ),
    ]