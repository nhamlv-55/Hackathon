import os.path

from django.views.generic import TemplateView, RedirectView

from django.conf.urls import patterns, include, url

from django.contrib import admin

from tracker.views import *

from pakdd.views import *
admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(__file__), '../site_media'
)
tracker_csv = os.path.join(
    os.path.dirname(__file__), '../tracker/csv'
)
urlpatterns = patterns('',
    # Examples:
    (r'^$', main_page),
    (r'^test/$', test),
    (r'^q2/$', q2),
    (r'^creative/$', creative),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    (r'^tracker_csv/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': tracker_csv }),
    (r'^loan_shark/$', loan_shark),
    (r'^pakdd/$', pakdd),
    (r'^pakdd/vis', result),
    # querry part
    # (r'^search/$', search_page),

    url(r'^admin/', include(admin.site.urls)),
)
