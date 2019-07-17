from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chart_messages, name='chat')
]