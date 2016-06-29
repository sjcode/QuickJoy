#!/usr/bin/python
__author__ = 'sujian'
# -*- coding: UTF-8 -*-

from django.db import models
from django.db import models
from django.contrib import admin

# Create your models here.

class forum(models.Model):
    title = models.CharField('title',max_length=256)
    description = models.CharField('description',max_length=512)

    iconurl = models.URLField('iconurl')
    fid = models.IntegerField(unique=True,blank=False)


'''
class MVUser(models.Model):
    username = models.CharField('username', max_length=30, unique=True)
    password = models.CharField('password', max_length=128)
    gender = models.CharField(default='unknown',max_length=30)
    registerdate = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ('registerdate',)
'''


