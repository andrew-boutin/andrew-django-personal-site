from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # /pcbuild/
    url(r'^pcbuild/$', views.pcbuild, name='pcbuild'),
    # /gamedev/
    url(r'^gamedev/$', views.gamedev, name='gamedev'),
    # /keyboard/
    url(r'^keyboard/$', views.keyboard, name='keyboard'),
]
