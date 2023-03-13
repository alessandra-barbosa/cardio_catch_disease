# Generated by Django 3.1.3 on 2020-11-09 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='active',
            field=models.IntegerField(blank=True, choices=[(0, 'Sedentary'), (1, 'Active Person')], null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='alcohol',
            field=models.IntegerField(blank=True, choices=[(0, 'NO'), (1, 'YES')], null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='cholesterol',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)], null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2)], null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='glucose',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)], null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='hight_pressure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='low_pressure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='patients',
            name='smoker',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'YES')], null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='cardio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]
