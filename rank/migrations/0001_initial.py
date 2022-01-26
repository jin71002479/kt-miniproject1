# Generated by Django 2.2.5 on 2022-01-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rank_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('user_score', models.IntegerField()),
                ('user_name', models.TextField()),
            ],
            options={
                'ordering': ['-user_score'],
            },
        ),
    ]
