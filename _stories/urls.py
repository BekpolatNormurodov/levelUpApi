from django.urls import path
from _stories.stories import Stories
from _stories.story_test import StoryTest
from _stories.vocabulary import Vocabulary
from _stories.vocabulary_test import VocabularyTest
from _stories.vocabulary_full import VocabularyFull
from _stories.vocabulary_line import VocabularyLine
from _stories.vocabulary_find import VocabularyFind

urlpatterns = [
    # STORIES
    path('', Stories.as_view()),
    path('test/', StoryTest.as_view()),
    path('vocabulary/', Vocabulary.as_view()),
    path('vocabularyTest/', VocabularyTest.as_view()),
    path('vocabularyfull/', VocabularyFull.as_view()),
    path('vocabularyline/', VocabularyLine.as_view()),
    path('vocabularyfind/', VocabularyFind.as_view()),
]