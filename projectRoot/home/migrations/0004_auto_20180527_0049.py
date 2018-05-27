# Generated by Django 2.0.5 on 2018-05-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180526_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type_name', models.CharField(max_length=20)),
                ('beer', models.ManyToManyField(blank=True, to='home.Beer')),
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
        migrations.RemoveField(
            model_name='containeroption',
            name='beer',
        ),
        migrations.RemoveField(
            model_name='tasteoption',
            name='beer',
        ),
        migrations.DeleteModel(
            name='ContainerOption',
        ),
        migrations.DeleteModel(
            name='TasteOption',
        ),
    ]
