# Generated by Django 4.1.7 on 2023-07-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlredirection',
            name='urlname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]