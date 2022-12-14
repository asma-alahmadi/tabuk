# Generated by Django 4.1 on 2022-08-17 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabuk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('total_price', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tabuk.package')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('adults', models.IntegerField(default=1)),
                ('children', models.IntegerField(blank=True, default=0, null=True)),
                ('start_date', models.DateField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabuk.package')),
            ],
        ),
    ]
