from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from portal.views import *
from django.views.generic.base import RedirectView

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='home/'), name="index_page"),

    url(r'^home/$', ListTutorial.as_view(), name="home"),
    url(r'^detail/(?P<pk>\d+)$', ViewPost.as_view(), name="detail"),
    url(r'^category/(?P<pk>\d+)$', CategoryList.as_view(), name="category"),
    url(r'^search/$', SearchView.as_view(), name="search"),

    url(r'^post$', PostView.as_view(), name="post"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^statis/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
