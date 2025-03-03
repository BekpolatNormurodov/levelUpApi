from django.urls import path
from .views import *

urlpatterns = [
    path('story/', StoryApiView.as_view()),
    path('vocabulary/', VocabularyApiView.as_view()),
]