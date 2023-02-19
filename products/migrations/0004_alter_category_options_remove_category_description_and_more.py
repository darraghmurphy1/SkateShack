# Generated by Django 4.1.5 on 2023-02-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_remove_skateboardaccessories_skateboard_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]