from rest_framework.response import Response
from rest_framework.views import APIView

class StoryApiView(APIView):
    def get(self, request):
        story_1 = {"title": "Level-1", "story": ["a", "b", "c", "d"], "images": [""]}
        story_2 = {"title": "Level-2", "story": ["aa", "ab", "ac", "ad"], "images": [""]}

        data = [
            story_1, 
            story_2,
        ]
        return Response(data)
    


class VocabularyApiView(APIView):
    def get(self, request):
        vocabulary_1 = {"vocabulary_en": ["a", "b", "c", "d"], "vocabulary_uz": ["a", "b", "c", "d"], "sentence_en": ["a", "b", "c", "d"], "sentence_uz": ["a", "b", "c", "d"],}
        vocabulary_2 = {"vocabulary_en": ["a", "b", "c", "d"], "vocabulary_uz": ["a", "b", "c", "d"], "sentence_en": ["a", "b", "c", "d"], "sentence_uz": ["a", "b", "c", "d"],}

        data = [
            vocabulary_1, 
            vocabulary_2,
        ]
        return Response(data)