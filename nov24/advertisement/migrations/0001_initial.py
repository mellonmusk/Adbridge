# Generated by Django 5.1.3 on 2024-11-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(default='product.svg', upload_to='advertisement/')),
                ('title', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default='description of the product')),
                ('min_budget', models.PositiveIntegerField(default=0)),
                ('max_budget', models.PositiveIntegerField(default=0)),
                ('detail_1', models.ImageField(default='product.svg', upload_to='advertisement/')),
                ('detail_2', models.ImageField(default='product.svg', upload_to='advertisement/')),
            ],
        ),
    ]
