from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.camera,
        name='photo',
    ),
    url(
        regex=r'^image$',
        view=views.image,
        name='image',
    ),
    url(
        regex=r'^snapshot$',
        view=views.take_snapshot,
        name='snapshot',
    ),
]