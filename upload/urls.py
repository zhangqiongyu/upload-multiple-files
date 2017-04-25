from django.conf.urls import url, include

from upload import views

urlpatterns = [
    url(r'form/$', views.form),
    url(r'upload/$', views.upload),
]