# Generated by Django 2.0.5 on 2018-05-28 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_name', models.CharField(max_length=50)),
                ('colour_srm_value', models.FloatField(default=0.0)),
                ('alcohol_by_volume', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('country_of_origin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContainerStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_style_name', models.CharField(max_length=20)),
                ('beer', models.ManyToManyField(blank=True, to='home.Beer')),
            ],
        ),
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taste_name', models.CharField(max_length=50)),
                ('beer', models.ManyToManyField(blank=True, to='home.Beer')),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='body_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.BodyType'),
        ),
        migrations.AddField(
            model_name='beer',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Brand'),
        ),
    ]