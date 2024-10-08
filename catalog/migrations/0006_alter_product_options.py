# Generated by Django 5.1.1 on 2024-09-27 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "name"],
                "permissions": [
                    ("can_edit_category", "can_edit_category"),
                    ("can_edit_description", "can_edit_description"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
