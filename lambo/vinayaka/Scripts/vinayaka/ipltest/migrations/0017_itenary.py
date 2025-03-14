# Generated by Django 3.0.4 on 2020-08-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipltest', '0016_delete_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itenary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Match_no', models.IntegerField()),
                ('Teams', models.CharField(blank=True, max_length=255, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Day', models.CharField(blank=True, max_length=255, null=True)),
                ('Time', models.CharField(blank=True, max_length=255, null=True)),
                ('Venue', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'ipl_itenary',
                'managed': False,
            },
        ),
    ]
