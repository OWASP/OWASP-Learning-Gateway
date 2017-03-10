from django.conf.urls import include, url
from website.views import UserProfileDetailView, DashboardView
from django.contrib import admin
admin.autodiscover()

import website.views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', website.views.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/$', website.views.profile, name='profile'),
    url(r'^dashboard/$', login_required(DashboardView.as_view()), name="dashboard"),
    url(r'^profile/(?P<slug>[^/]+)/$', UserProfileDetailView.as_view(), name="profile"),
]
