# Generated by Django 5.0.2 on 2024-06-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Otklonil', 'Otklonil')], default='Pending', max_length=20),
        ),
    ]
