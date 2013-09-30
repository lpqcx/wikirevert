from django.conf.urls import patterns, include, url

from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'revert_interface.views.home', name='home'),
    # url(r'^revert_interface/', include('revert_interface.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^wiki/(.+)$', wiki_page),
    url(r'^edit/(.+)$', wiki_edit_page),
    url(r'^w/index.php$', wiki_index_php),
    url(r'^w/api.php$', wiki_api_php),
)
