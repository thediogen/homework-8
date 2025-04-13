# Generated by Django 5.2 on 2025-04-13 17:40

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
                ('motto', models.CharField(max_length=128)),
                ('meeting_room', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LibCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateField(default=datetime.datetime(2025, 4, 13, 17, 40, 10, 201501, tzinfo=datetime.timezone.utc))),
                ('end_date', models.DateField(default=datetime.datetime(2025, 5, 13, 17, 40, 10, 201501, tzinfo=datetime.timezone.utc))),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=128)),
                ('books', models.ManyToManyField(to='university.book')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('student_card_num', models.PositiveIntegerField()),
                ('addres', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='university.group')),
                ('lib_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.libcard')),
            ],
        ),
        migrations.CreateModel(
            name='OweBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owe_date', models.DateField(default=datetime.datetime(2025, 4, 13, 17, 40, 10, 201980, tzinfo=datetime.timezone.utc))),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.book')),
                ('lib_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.libcard')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student')),
            ],
        ),
    ]
