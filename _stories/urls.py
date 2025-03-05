from django.urls import path
from _stories.stories import Stories
from _stories.vocabulary import Vocabulary

urlpatterns = [
    path('stories/', Stories.as_view()),
    path('vocabulary/', Vocabulary.as_view()),
]