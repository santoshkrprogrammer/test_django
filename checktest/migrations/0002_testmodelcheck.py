# Generated by Django 4.0 on 2024-04-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testmodelcheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_check', models.CharField(max_length=123)),
            ],
        ),
    ]
