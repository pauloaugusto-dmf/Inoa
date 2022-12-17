# Generated by Django 4.1.4 on 2022-12-16 04:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'stock',
                'verbose_name_plural': 'stocks',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='market.stock')),
            ],
            options={
                'verbose_name': 'quote',
                'verbose_name_plural': 'quotes',
            },
        ),
    ]
