from rest_framework.response import Response
from rest_framework.views import APIView
    
class VocabularyFind(APIView):
    def get(self, request):
        find_1 = [
                    {
                "en": "that",
                "uz": "u, ana u (uzoqda)",
                "index": 0
            },
            {
                "en": "this",
                "uz": "bu, mana bu (yonida)",
                "index": 1
            },
        ],
        find_2 = [
                   {
                "en": "that",
                "uz": "u, ana u (uzoqda)",
                "index": 0
            },
            {
                "en": "this",
                "uz": "bu, mana bu (yonida)",
                "index": 1
            },
        ],
        data = [
            find_1,
            find_2,
        ]
        return Response(data)