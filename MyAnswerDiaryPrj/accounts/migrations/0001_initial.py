# Generated by Django 4.0.6 on 2022-08-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15)),
                ('user_pw', models.CharField(max_length=128)),
                ('user_name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': '유저',
            },
        ),
    ]
