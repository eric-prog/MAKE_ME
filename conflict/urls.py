from django.urls import path
from . import views

app_name = 'conflict'
 
urlpatterns = [ 
    path('', views.alltop, name = 'all-top'),
    path('top-100/', views.top100, name = 'top-100'),
    path('top-trend/', views.toptrend, name = 'top-trend'), 
    path('create/', views.conflict_create, name = 'create'),
    path('<slug:slug>/', views.conflict_detail, name = 'detail'), 
]
  