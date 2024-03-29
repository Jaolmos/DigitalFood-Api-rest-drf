# Generated by Django 4.2.4 on 2024-01-01 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_type', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], max_length=200)),
                ('status_payment', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.table')),
            ],
        ),
    ]
