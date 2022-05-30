from django.contrib import admin
from django.urls import path
from semanticAnalysis import views
urlpatterns = [
    path('',views.semantic, name='semantic'),

]
