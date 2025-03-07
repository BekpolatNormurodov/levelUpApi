from rest_framework.response import Response
from rest_framework.views import APIView
    
class VocabularyFull(APIView):
    def get(self, request):
        full_1 = [
            {
                "en": "yours",
                "uz": "seniki"
            },
            {
                "en": "his",
                "uz": "uniki (erkak)"
            },
        ],   
        full_2 = [
            {
                "en": "yours",
                "uz": "seniki"
            },
            {
                "en": "his",
                "uz": "uniki (erkak)"
            },
        ],
      
        data = [
            full_1,
            full_2,
        ]
        return Response(data) 