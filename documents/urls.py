from django.conf.urls import url

import views

urlpatterns = [
    url(
        r'^print/(?P<proform_id>\d+)/',
        views.index,
        name='print'
    ),
]
