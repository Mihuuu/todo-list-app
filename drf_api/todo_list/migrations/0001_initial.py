# Generated by Django 2.0.4 on 2018-09-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=50)),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.BooleanField(default=False)),
                ('expire_date', models.DateTimeField(null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '待办项目',
                'db_table': 'todo',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'db_table': 'user',
            },
        ),
    ]
