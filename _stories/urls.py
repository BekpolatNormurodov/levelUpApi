from django.urls import path
from _conversation.vocabulary_find import VocabularyFind
from _conversation.vocabulary_full import VocabularyFull
from _conversation.vocabulary_line import VocabularyLine
from _conversation.vocabulary_test import VocabularyTest
from _stories.stories import Stories
from _stories.story_test import StoryTest
from _stories.vocabulary import Vocabulary

urlpatterns = [
    # STORIES
    path('stories/', Stories.as_view()),
    path('storytest/', StoryTest.as_view()),
    path('vocabulary/', Vocabulary.as_view()),
    path('VocabularyTest/', VocabularyTest.as_view()),
    path('storiesfull/', VocabularyFull.as_view()),
    path('storiesline/', VocabularyLine.as_view()),
    path('storiesfind/', VocabularyFind.as_view()),
]