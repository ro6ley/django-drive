from django.conf.urls import url

from .views import CarView


urlpatterns = [
  url(r'^cars/$', CarView.as_view(), name="cars"),
]
