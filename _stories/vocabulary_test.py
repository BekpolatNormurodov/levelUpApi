from rest_framework.response import Response
from rest_framework.views import APIView

class VocabularyTest(APIView):
    def get(self, request):
        test_1 = [
            {
                "question": "u (qiz)",
                "options": [
                    "he",
                    "she",
                    "it",
                    "they"
                ],
                "answer": "she"
            },
            {
                "question": "u",
                "options": [
                    "it",
                    "he",
                    "she",
                    "they"
                ],
                "answer": "it"
            },
        ],
        test_2 = [
            {
                "question": "u (qiz)",
                "options": [
                    "he",
                    "she",
                    "it",
                    "they"
                ],
                "answer": "she"
            },
            {
                "question": "u",
                "options": [
                    "it",
                    "he",
                    "she",
                    "they"
                ],
                "answer": "it"
            },
        ],
        data = [
            test_1,
            test_2,
        ]
        return Response(data)