from django.urls import path
from .views import (
    ClientListCreateView, ClientRetrieveUpdateDestroyView,
    ProjectListCreateView, UserProjectsView, ProjectRetrieveDestroyView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveDestroyView.as_view(), name='project-detail'),
    path('projects/assigned/', UserProjectsView.as_view(), name='user-projects'),
]
