# Generated by Django 5.1.2 on 2024-11-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_contract_property_alter_contract_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='buyer',
        ),
        migrations.AddField(
            model_name='property',
            name='descriprion',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]