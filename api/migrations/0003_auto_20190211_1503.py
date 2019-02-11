# Generated by Django 2.1 on 2019-02-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('team', models.CharField(max_length=3)),
                ('team_preffered_name', models.CharField(max_length=25)),
                ('team_name', models.CharField(max_length=25)),
                ('team_city', models.CharField(max_length=25)),
                ('team_conference', models.CharField(max_length=5)),
                ('team_conference_division', models.CharField(max_length=15)),
                ('team_logo_id', models.IntegerField()),
                ('Team_hex_color', models.CharField(max_length=8)),
                ('team_hex_alt_color', models.CharField(max_length=8)),
                ('Name', models.CharField(max_length=30)),
                ('Position', models.CharField(max_length=2)),
                ('position_name', models.CharField(max_length=12)),
                ('position_type', models.CharField(max_length=3)),
                ('encounter', models.CharField(max_length=12)),
                ('category', models.CharField(max_length=20)),
                ('crime_category', models.CharField(max_length=20)),
                ('crime_category_color', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=2000)),
                ('outcome', models.CharField(max_length=2000)),
                ('season', models.IntegerField()),
                ('arrestseasonstate', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('day_of_week', models.CharField(max_length=10)),
                ('day_of_week_int', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['arrest_count']},
        ),
    ]
