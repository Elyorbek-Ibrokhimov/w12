from django.urls import path
from . import views

urlpatterns = [
    path('', views.maktab_list, name='maktab_list'),
    path('maktab/<int:pk>/', views.maktab_detail, name='maktab_detail'),
    path('maktab/new/', views.maktab_create, name='maktab_create'),
    path('maktab/<int:pk>/edit/', views.maktab_edit, name='maktab_edit'),
    path('maktab/<int:pk>/delete/', views.maktab_delete, name='maktab_delete'),
    path('sinf/<int:pk>/', views.sinf_detail, name='sinf_detail'),
    path('maktab/<int:maktab_pk>/sinf/new/', views.sinf_create, name='sinf_create'),
    path('sinf/<int:pk>/edit/', views.sinf_edit, name='sinf_edit'),
    path('sinf/<int:pk>/delete/', views.sinf_delete, name='sinf_delete'),
    path('sinf/<int:sinf_pk>/student/new/', views.student_create, name='student_create'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
