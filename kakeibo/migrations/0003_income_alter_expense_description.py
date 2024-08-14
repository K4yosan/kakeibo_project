# Generated by Django 5.1 on 2024-08-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0002_alter_expense_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
