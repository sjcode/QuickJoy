
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin



urlpatterns = patterns('',

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('forum.urls')),
    url(r'^',include('account.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)

