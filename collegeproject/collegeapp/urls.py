from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('person/',views.person_id,name='person'),
    path('get-couses/', views.GetCourses, name='get_couses'),
    path('confirm/',views.confirm,name='confirm'),
]
