from django.conf.urls import url
from helloapp.views import hello, hello2, hello3
urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^(?P<id>[0-9]+)/hello2/$', hello2),
    url(r'^hello3/$', hello3)
]