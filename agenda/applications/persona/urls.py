from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('lista-personas/', views.PersonTempListView.as_view(), name='lista_personas'),
    path('api/persona/lista/', views.PersonListApiView.as_view()),
    path('lista/', views.PersonListView.as_view(), name='lista'),
    path('api/persona/search/<kword>/', views.PersonSearchApiView.as_view(), name='search'),
    path('api/persona/create/', views.PersonCreateView.as_view(), name='create'),
    path('api/persona/detail/<pk>/', views.PersonRetrieveApiView.as_view(), name='detail'),
    path('api/persona/delete/<pk>/', views.PersonDeleteView.as_view(), name='delete'),
    
]
