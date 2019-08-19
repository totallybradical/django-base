# Generated by Django 2.2.4 on 2019-08-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='primary_strength',
            field=models.CharField(choices=[('ADV', 'Advisor'), ('CON', 'Connector'), ('CRE', 'Creator'), ('EQU', 'Equalizer'), ('INF', 'Influencer'), ('PIO', 'Pioneer'), ('PRO', 'Provider'), ('STI', 'Stimulator'), ('TEA', 'Teacher')], max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(choices=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West')], max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='secondary_strength',
            field=models.CharField(choices=[('ADV', 'Advisor'), ('CON', 'Connector'), ('CRE', 'Creator'), ('EQU', 'Equalizer'), ('INF', 'Influencer'), ('PIO', 'Pioneer'), ('PRO', 'Provider'), ('STI', 'Stimulator'), ('TEA', 'Teacher')], max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='team',
            field=models.CharField(choices=[('COMM', 'Commercial'), ('USPS', 'Public Sector')], max_length=4),
        ),
    ]