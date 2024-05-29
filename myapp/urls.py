from django.urls import path
from . import views

urlpatterns = [
    path('', views.location_view, name='location-view'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-schools/', views.load_schools, name='ajax_load_schools'),
    path('ajax/load-sinf/', views.load_sinf, name='ajax_load_sinf'),
    path('students/', views.student_list, name='student-list'),
    path('add_student/', views.add_student, name='add-student'),
    path('success/', views.success, name='success'),
]
