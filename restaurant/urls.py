#define URL route for index() view
from django.urls import path
from .views import UserList,MenuItemsView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('users/', UserList.as_view(), name='user-list'),
    path('api-token-auth/', obtain_auth_token),

  ]
