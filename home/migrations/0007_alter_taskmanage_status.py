# Generated by Django 4.2.6 on 2023-10-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_taskmanage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmanage',
            name='status',
            field=models.CharField(choices=[('Completed', 'C'), ('InProgress', 'IP'), ('Pending', 'P')], max_length=100),
        ),
    ]
