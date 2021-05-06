from django.urls import path

from . import views

urlpatterns = [
    path('write/', views.write, name="write"),
    path('list/', views.list, name="list"),
    path('list/<int:num>/', views.view, name="view"),
    path('hello/', views.helloAPI),
]
