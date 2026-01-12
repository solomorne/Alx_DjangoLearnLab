from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Route for the function-based view
    path('books/', list_books, name='list_books'),
    
    # Route for the class-based view
    # <int:pk> is the primary key of the Library you want to view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    # Auth URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Existing URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    # ... existing URLs ...
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]