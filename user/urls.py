from django.urls import path, include
from . import views
from .views import (
    BillBoardCreateView, 
    BillBordListView, 
    BillBoardDeleteView, 
    BillBoardUpdateView, 
    BillBordSearchView,
    BillBordFilterView
    )
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

# #set namespace
app_name = 'user'

urlpatterns = [    
    path('',views.BillBordListView.as_view(), name='BillBord_list'),
    path('new/',views.BillBoardCreateView.as_view(), name='create_BillBord'),
    path('<int:pk>/delete/', BillBoardDeleteView.as_view(), name='delete_BillBoard'),  
    path('<int:pk>/edit/', BillBoardUpdateView.as_view(), name='edit_BillBoard'),  
    path('search/', BillBordSearchView.as_view(), name='search_BillBoard'),  
    path('filter/', BillBordFilterView.as_view(), name='filter_BillBoard'),  
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'), 
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)