from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('book/', views.Book_list),
    path('book/<int:pk>/', views.Book_detail),
    path('member/', views.Member_list),
    path('member/<int:pk>/', views.Member_detail),
    path('borrow/', views.Borrow_list),
    path('borrow/<int:pk>/', views.Borrow_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
