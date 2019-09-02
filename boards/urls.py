from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# #set namespace
app_name = 'boards'

from rest_framework import routers

router = routers.DefaultRouter()
router.register('listboards',views.listboards)#mension path in space given between''
router.register('city',views.listCities)#mension path in space given between''
router.register('contact',views.listconatct)
urlpatterns = [
    path('',include(router.urls)), 
    path('hander', views.handler), 
    path('contact',views.listconatct),
    # path('city',citylistview.as_view(), name='city'), 

      
]
if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns()
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)