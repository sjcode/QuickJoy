# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('announce_from', models.DateTimeField(null=True, verbose_name='Announce from', blank=True)),
                ('announce_to', models.DateTimeField(null=True, verbose_name='Announce to', blank=True)),
                ('created_by', models.ForeignKey(related_name='announcers', editable=False, to=settings.AUTH_USER_MODEL)),
                ('mark_as_read', models.ManyToManyField(related_name='announcements', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='forum.Category')),
                ('created_by', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('reply_to', models.ForeignKey(related_name='child', blank=True, to='forum.Post', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
