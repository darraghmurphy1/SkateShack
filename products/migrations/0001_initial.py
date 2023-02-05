# Generated by Django 4.1.5 on 2023-02-05 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skateboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='skateboard_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='SkateboardWheels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('width', models.FloatField()),
                ('image', models.ImageField(upload_to='wheels_images/')),
                ('skateboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.skateboard')),
            ],
        ),
        migrations.CreateModel(
            name='SkateboardTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('width', models.FloatField()),
                ('image', models.ImageField(upload_to='truck_images/')),
                ('skateboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.skateboard')),
            ],
        ),
        migrations.CreateModel(
            name='SkateboardHardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='hardware_images/')),
                ('skateboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.skateboard')),
            ],
        ),
        migrations.CreateModel(
            name='SkateboardDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100)),
                ('width', models.FloatField()),
                ('length', models.FloatField()),
                ('image', models.ImageField(upload_to='deck_images/')),
                ('skateboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.skateboard')),
            ],
        ),
    ]
