from django.urls import path,include
from . import views

app_name='whiskyApp'
# urlpatterns += [
urlpatterns = [
    path('', views.index, name="index"),
]
