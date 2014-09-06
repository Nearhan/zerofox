from django.conf.urls import patterns, include, url
from resumes.views import WelcomeView, CreateUserView, ResumeView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zerofox.views.home', name='home'),
    url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^(?P<created>created=True)$', WelcomeView.as_view(), name='welcome'),
    url(r'^signIn', CreateUserView.as_view(), name='sign_in'),
    url(r'^resume', ResumeView.as_view(), name='resume')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
