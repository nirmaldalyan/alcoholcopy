# Generated by Django 4.0.5 on 2022-07-08 01:45

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_title', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50)),
                ('service_des', tinymce.models.HTMLField()),
            ],
        ),
    ]
