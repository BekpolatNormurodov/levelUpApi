from django.urls import path
from _conversation.conversation import Conversation
from _conversation.conversation_test1 import ConversationTest1
from _conversation.conversation_test2 import ConversationTest2
from _conversation.vocabulary import Vocabulary
from _conversation.vocabulary_find import VocabularyFind
from _conversation.vocabulary_full import VocabularyFull
from _conversation.vocabulary_line import VocabularyLine
from _conversation.vocabulary_test import VocabularyTest

urlpatterns = [
    # CONVERSATION
    path('', Conversation.as_view()),
    path('test1/', ConversationTest1.as_view()),
    path('test2/', ConversationTest2.as_view()),
    path('vocabulary/', Vocabulary.as_view()),
    path('vocabularyTest/', VocabularyTest.as_view()),
    path('vocabularyfull/', VocabularyFull.as_view()),
    path('vocabularyline/', VocabularyLine.as_view()),
    path('vocabularyfind/', VocabularyFind.as_view()),
]