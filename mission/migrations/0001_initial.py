# Generated by Django 4.2.15 on 2024-08-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('robot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robot.robot')),
            ],
        ),
    ]
