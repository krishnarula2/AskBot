# chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_with_bot, name='chat'),
    path('', views.chat_ui, name='chat_ui'),  # <-- this serves the page
]
