from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'web.views.index', name="index"),
]
