# Generated by Django 3.0.5 on 2020-06-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200530_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=500)),
                ('email', models.CharField(default='', max_length=50)),
                ('qury', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]
