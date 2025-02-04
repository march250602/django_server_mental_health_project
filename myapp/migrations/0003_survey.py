# Generated by Django 5.1.5 on 2025-02-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_1', models.CharField(max_length=1)),
                ('Question_2', models.CharField(max_length=1)),
                ('Question_3', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'survey',
            },
        ),
    ]
