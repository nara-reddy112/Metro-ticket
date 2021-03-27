# Generated by Django 2.0 on 2021-03-26 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210326_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Junction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jun_name', models.CharField(max_length=200)),
                ('lane_type', models.PositiveIntegerField()),
                ('lane_type2', models.PositiveIntegerField()),
                ('entry_jun_lane_type_num', models.PositiveIntegerField()),
                ('exit_jun_lane_type_num2', models.PositiveIntegerField()),
                ('lane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Lane')),
            ],
        ),
        migrations.AlterField(
            model_name='bluelane',
            name='blue_extra_price',
            field=models.FloatField(default=2),
        ),
    ]