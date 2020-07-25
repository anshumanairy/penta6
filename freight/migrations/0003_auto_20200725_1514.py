# Generated by Django 3.0.8 on 2020-07-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freight', '0002_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='destination_address',
            field=models.TextField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='quotes',
            name='destination_pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quotes',
            name='origin_address',
            field=models.TextField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='quotes',
            name='origin_pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quotes',
            name='quantity',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='c_type',
            field=models.CharField(choices=[('', 'Select an option'), ('L', 'Land'), ('A', 'Air'), ('O', 'Ocean')], max_length=10),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='goods',
            field=models.CharField(max_length=30),
        ),
    ]