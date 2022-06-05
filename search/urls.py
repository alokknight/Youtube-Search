from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# app_name='search'
router = routers.DefaultRouter()
router.register(r'searchdata', views.SearchdataViewSet,'searchdata')
router.register(r'searchindex', views.SearchindexViewSet,'searchindex')
searchrouter=router
# urlpatterns=router.urls
app_name='search'
urlpatterns = [
    # API url
    # path('api/', include(router.urls)),
    path(''           ,views.index, name='index'),
    path('asyncfun/'  ,views.asyncfun, name='asyncfun'),
    path('show/'      ,views.show,name='show'),
    path('fetch/'     ,views.fetch,name='fetch'),
    path('list/'      ,views.listing,name='list'),
    path('changeflag/',views.changeflagTofalse,name='changeflag'),
]

urlpatterns = format_suffix_patterns(urlpatterns)