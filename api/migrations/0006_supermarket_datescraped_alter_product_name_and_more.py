# Generated by Django 4.2.3 on 2023-09-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_alter_product_name_alter_product_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="supermarket",
            name="dateScraped",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="product",
            name="shelve",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="product",
            name="sub_department",
            field=models.CharField(max_length=255),
        ),
    ]
