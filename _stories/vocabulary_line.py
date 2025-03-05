from rest_framework.response import Response
from rest_framework.views import APIView
      
class VocabularyLine(APIView):
    def get(self, request):
        random_1 = [
                    "those",
                    "himself",
                    "hers",
                    "these",
                    "ourselves",
                    "theirs",
                    "themselves",
                    "his",
                    "herself",
                    "ours"
        ],
        random_2 = [
                    "those",
                    "himself",
                    "hers",
                    "these",
                    "ourselves",
                    "theirs",
                    "themselves",
                    "his",
                    "herself",
                    "ours"
        ],
        data = [
            random_1,
            random_2,
        ]
        return Response(data)