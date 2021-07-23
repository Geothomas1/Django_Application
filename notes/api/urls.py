from django.urls import path
from .import views
urlpatterns=[
    path('',views.getRoute),
    path('notes/',views.getNotes),
    path('notes/create/',views.createNote),
    path('notes/update/<str:pk>/',views.updateNotebyId),
    path('notes/delete/<str:pk>/',views.deleteNote),
    path('notes/<str:pk>/',views.getNotesbyId)
]