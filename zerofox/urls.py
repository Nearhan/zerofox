from django.conf.urls import patterns, url
from resumes.views import (
    WelcomeView, CreateUserView, ResumeDetailView, ResumeCreateView,
    JobCreateView
)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zerofox.views.home', name='home'),
    url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^(?P<created>created=True)$', WelcomeView.as_view(), name='welcome'),
    url(r'^signUp', CreateUserView.as_view(), name='sign_up'),
    url(r'^resume', ResumeDetailView.as_view(), name='resume_list'),
    url(r'^create_resume', ResumeCreateView.as_view(), name='create_resume'),
    url(r'^add_position', JobCreateView.as_view(), name='create_job')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
