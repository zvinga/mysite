# Generated by Django 3.0.6 on 2020-06-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='x',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]