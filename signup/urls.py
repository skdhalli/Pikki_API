from django.conf.urls import url
from signup import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^account/$', views.Account.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
