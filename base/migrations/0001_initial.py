# Generated by Django 5.0.2 on 2024-04-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BattleRoyale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('Rank', models.CharField(max_length=150)),
                ('kd_ratio', models.FloatField()),
                ('headshot_rate', models.FloatField()),
                ('no_of_headshots', models.IntegerField()),
                ('top_3_ratio', models.FloatField()),
                ('Avg_damage', models.FloatField()),
            ],
        ),
    ]
