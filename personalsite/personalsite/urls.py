"""Site's main url routing point - route to the appropriate app views."""
from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^', include('main.urls')),
    url(r'^admin/', admin.site.urls),
]

# Override Django's default error pages and re-wire to custom views
site_view = 'personalsite.views.'

handler400 = site_view + 'bad_request'
handler403 = site_view + 'permission_denied'
handler404 = site_view + 'page_not_found'
handler500 = site_view + 'error'

if settings.DEBUG:
    # Wire up views to serve static files easily while developing
    urlpatterns += staticfiles_urlpatterns()

    # Allows the custom error pages to be viewed while developing
    urlpatterns += [
        url(r'^400/$', TemplateView.as_view(template_name='400.html')),
        url(r'^403/$', TemplateView.as_view(template_name='403.html')),
        url(r'^404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    ]

