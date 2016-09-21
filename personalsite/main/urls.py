from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # /devprojects/
    url(r'^devprojects/$', views.devprojects, name='devprojects'),
    # /pcbuild/
    url(r'^pcbuild/$', views.pcbuild, name='pcbuild'),
    # /gamedev/
    url(r'^gamedev/$', views.gamedev, name='gamedev'),
    # /gamedev/pirates/
    url(r'^gamedev/pirates/$', views.pirates, name='pirates'),
    # /gamedev/labyrinthcrawl/
    url(r'^gamedev/labyrinthcrawl/$', views.labyrinthcrawl, name='labyrinthcrawl'),
    # /gamedev/epiccrawl/
    url(r'^gamedev/epiccrawl/$', views.epiccrawl, name='epiccrawl'),
    # /gamedev/geowars/
    url(r'^gamedev/geowars/$', views.geowars, name='geowars'),
    # /gamedev/squares/
    url(r'^gamedev/squares/$', views.squares, name='squares'),
    # /keyboard/
    url(r'^keyboard/$', views.keyboard, name='keyboard'),
]
