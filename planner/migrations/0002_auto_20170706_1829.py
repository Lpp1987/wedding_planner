# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-06 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planner.AppUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planner.AppUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photographer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planner.AppUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddinghall',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planner.AppUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddingrings',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planner.AppUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='band',
            name='cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='band',
            name='paid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='to_pay',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='paid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='to_pay',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='paid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='to_pay',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='weddinghall',
            name='cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='weddinghall',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='weddinghall',
            name='paid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='weddinghall',
            name='to_pay',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='weddingrings',
            name='cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='weddingrings',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='weddingrings',
            name='paid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='weddingrings',
            name='to_pay',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='wedding',
            name='Band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Band'),
        ),
        migrations.AddField(
            model_name='wedding',
            name='Car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Car'),
        ),
        migrations.AddField(
            model_name='wedding',
            name='Photographer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Photographer'),
        ),
        migrations.AddField(
            model_name='wedding',
            name='WeddingHall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.WeddingHall'),
        ),
        migrations.AddField(
            model_name='wedding',
            name='WeddingRings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.WeddingRings'),
        ),
        migrations.AddField(
            model_name='wedding',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.AppUser'),
        ),
    ]