from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserCreateView.as_view()),
    path('details/', views.UserDetailView.as_view()),
    path('push/', views.DeviceView.as_view())
]