# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = [
    # Public pages
    url(r'^$', 'pyscada.hmi.views.index'),
    url(r'^accounts/logout/$', 'pyscada.hmi.views.logout_view'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^json/cache_data/$', 'pyscada.hmi.views.get_cache_data'),
    url(r'^json/init_data/$', 'pyscada.hmi.views.data'),
    url(r'^json/log_data/$', 'pyscada.hmi.views.log_data'),
    url(r'^form/log_entry/$', 'pyscada.hmi.views.form_log_entry'),
    url(r'^form/write_task/$', 'pyscada.hmi.views.form_write_task'),
    url(r'^view/(?P<link_title>\w+)/$', 'pyscada.hmi.views.view',name="main-view"),
]
urlpatterns = patterns('', *urlpatterns)