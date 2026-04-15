from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_books),
    path('scrape/', views.scrape_and_store),
    path('ask/', views.ask_book),
    path('book/<int:id>/', views.get_book_detail),
]