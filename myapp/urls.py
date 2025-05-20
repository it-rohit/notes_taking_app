from django.urls import path
from .views import RegisterView, LoginView,LogoutView,NotesListCreateView, NotesDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('notes/', NotesListCreateView.as_view(), name='notes-list-create'),
    path('notes/<uuid:note_id>/', NotesDetailView.as_view(), name='notes-detail'),

]
