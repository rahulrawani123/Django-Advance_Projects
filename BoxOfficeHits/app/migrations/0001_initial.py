# Generated by Django 5.0 on 2024-01-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Movie', models.CharField(max_length=60)),
                ('Actor', models.CharField(max_length=50)),
                ('Actress', models.CharField(max_length=50)),
                ('Genre', models.CharField(max_length=60)),
                ('Payment', models.CharField(max_length=60)),
            ],
        ),
    ]