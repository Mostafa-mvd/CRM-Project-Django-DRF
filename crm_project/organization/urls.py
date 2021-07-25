from django.urls import path
from . import views

app_name = 'organization'

urlpatterns = [
    path('register/', views.CreateOrganization.as_view(), name="register"),
    path('list/', views.ListOrganization.as_view(), name="list"),
]