from django.urls import path

from . import views
urlpatterns = [
    path('create', views.OrderView.as_view(), name='create-order'),
    path('update/<int:pk>/', views.OrderView.as_view(), name='update-order'),
]
