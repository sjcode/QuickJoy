#-*-coding:utf-8-*- 
__author__ = 'sujian'

from rest_framework import permissions


class CategoryPermissions(permissions.BasePermission):
    """CategoryPermissions"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class PostPermissions(permissions.DjangoModelPermissions):
    """PostPermissions"""


class AnnouncementPermissions(permissions.DjangoModelPermissions):
    """AnnouncementPermissions"""

