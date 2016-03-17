# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-17 02:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.TextField(blank=True, max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Up', 'Up'), ('Down', 'Down')], max_length=4)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('content', models.TextField(blank=True, max_length=5000)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='IdeaCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Office', 'Office'), ('Food', 'Food'), ('Technical', 'Technical'), ('Hackathon', 'Hackathon'), ('Random', 'Random')], max_length=25)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Idea')),
            ],
        ),
        migrations.CreateModel(
            name='IdeaVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Up', 'Up'), ('Down', 'Down')], max_length=4)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Idea')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.AddField(
            model_name='ideavote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.User'),
        ),
        migrations.AddField(
            model_name='idea',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.User'),
        ),
        migrations.AddField(
            model_name='commentvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='idea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Idea'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.User'),
        ),
    ]