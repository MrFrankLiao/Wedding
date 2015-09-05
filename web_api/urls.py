from django.conf.urls import url, include, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from web_api import views_member

urlpatterns = format_suffix_patterns(patterns('',
                                              url(r'^login/$', views_member.Login.as_view(), name='login_action'),
))

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                        )