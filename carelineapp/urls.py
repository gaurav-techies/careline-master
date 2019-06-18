from django.urls import include, path

from . import views

urlpatterns = [
    path('topics', views.TopicListView.as_view()),
]