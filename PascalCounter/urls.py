from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'counter.views.home'),
    url(r'^new_session/$', 'counter.views.new_session'),
    url(r'^get_session/(\d+)/$', 'counter.views.get_session'),
    url(r'^api/increase/(\d+)/$', 'counter.views.session_api'),
    # url(r'^PascalCounter/', include('PascalCounter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
