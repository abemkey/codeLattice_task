from django.urls import path

from My_App import views

urlpatterns = [
        path("",views.home,name='home'),
        path('add_person/', views.add_person, name='add_person'),
        path('create_person/', views.create_person, name='create_person'),
        path('show_users/', views.show_users, name='show_users'),
        path('users_api/', views.users_api, name='users_api'),
]
