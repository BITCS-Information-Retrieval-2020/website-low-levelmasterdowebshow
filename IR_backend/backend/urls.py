from django.urls import path
from backend import views

urlpatterns = [
    path('integrated_search/', views.Integrated_search.as_view()),
    path('advanced_search/', views.Advanced_search.as_view()),
    path('paper_details/', views.Paper_details.as_view()),
    path('test/', views.Test.as_view()),
]
