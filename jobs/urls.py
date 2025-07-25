from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='home'),  # homepage shows jobs
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('applicant/dashboard/', views.applicant_dashboard, name='applicant_dashboard'),
]
