from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>', views.SchoolDetailView.as_view(), name='school-detail'),
    path('create', views.SchoolCreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'),
]