# Generated by Django 2.2 on 2019-02-20 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newbalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('realname', models.CharField(max_length=200)),
                ('accountNumber', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
    ]
