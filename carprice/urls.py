from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import routers
from . import views


app_name='carprice'
# router = routers.DefaultRouter()
# router.register(r'carprice', views.carprice,'carpriceapi')
# urlpatterns = carpricerouter.urls

# urlpatterns += [
urlpatterns = [
    path('',views.carprice,name='carprice'),
    path('carpricehome/',views.carpriceHome,name='carpricehome'),
    path('carpriceprediction/', views.carpriceprediction,name='carpriceprediction'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
