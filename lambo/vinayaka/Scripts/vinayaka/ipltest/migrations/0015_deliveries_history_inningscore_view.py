# Generated by Django 3.0.4 on 2020-04-18 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('ipltest', '0014_iplfinalview_topbatsmanview_topbowlersview'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('inning', models.IntegerField(blank=True, null=True)),
                ('batting_team', models.CharField(blank=True, max_length=255, null=True)),
                ('bowling_team', models.CharField(blank=True, max_length=255, null=True)),
                ('over', models.IntegerField(blank=True, null=True)),
                ('ball', models.IntegerField(blank=True, null=True)),
                ('batsman', models.CharField(blank=True, max_length=255, null=True)),
                ('non_striker', models.CharField(blank=True, max_length=255, null=True)),
                ('bowler', models.CharField(blank=True, max_length=255, null=True)),
                ('is_super_over', models.IntegerField(blank=True, null=True)),
                ('wide_runs', models.IntegerField(blank=True, null=True)),
                ('bye_runs', models.IntegerField(blank=True, null=True)),
                ('legbye_runs', models.IntegerField(blank=True, null=True)),
                ('noball_runs', models.IntegerField(blank=True, null=True)),
                ('penalty_runs', models.IntegerField(blank=True, null=True)),
                ('batsman_runs', models.IntegerField(blank=True, null=True)),
                ('extra_runs', models.IntegerField(blank=True, null=True)),
                ('total_runs', models.IntegerField(blank=True, null=True)),
                ('player_dismissed', models.CharField(blank=True, max_length=255, null=True)),
                ('dismisal_kind', models.CharField(blank=True, max_length=255, null=True)),
                ('fielder', models.CharField(blank=True, max_length=255, null=True)),
                ('wicket', models.IntegerField(blank=True, null=True)),
                ('matchid', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'deliveries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='inningscore_View',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstinning_score', models.IntegerField(blank=True, null=True)),
                ('secondinning_score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'inningscore_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType')),
            ],
        ),
    ]
