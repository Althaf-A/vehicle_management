"""vehicle_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('Account_login', views.Account_login, name='Account_login'),
    path('Account_Registrtion/', views.Account_Registrtion, name='Account_Registrtion'),
    
    path('User_Dashboard/', views.User_Dashboard, name='User_Dashboard'),
    path('User_logout/', views.User_logout, name='User_logout'),

    path('Admin_Dash/', views.Admin_Dash, name='Admin_Dash'),
    path('Admin_edit/<int:id>', views.Admin_edit, name='Admin_edit'),
    path('Admin_Update/<int:id>', views.Admin_Update, name='Admin_Update'),
    path('Admin_logout', views.Admin_logout, name='Admin_logout'),

    path('Super_Admin_Dash/', views.Super_Admin_Dash, name='Super_Admin_Dash'),
    path('Super_Admin_Vehicle_Add/', views.Super_Admin_Vehicle_Add,name='Super_Admin_Vehicle_Add'),
    path('Super_Admin_Vehicle_Registration/', views.Super_Admin_Vehicle_Registration,name='Super_Admin_Vehicle_Registration'),
    path('Super_Admin_edit/<int:id>', views.Super_Admin_edit, name='Super_Admin_edit'),
    path('Super_Admin_Update/<int:id>', views.Super_Admin_Update, name='Super_Admin_Update'),
    path('Super_Admin_Delete_Vehicle/<int:id>', views.Super_Admin_Delete_Vehicle, name='Super_Admin_Delete_Vehicle'),
    path('logout/', views.logout, name='logout'),
]
