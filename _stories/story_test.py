from rest_framework.response import Response
from rest_framework.views import APIView
    
class StoryTest(APIView):
    def get(self, request):
        test_1 = [
            {
                "question": "Who would I go for a walk outside on a hot day?",
                "options": [
                    "With my friend",
                    "With my brother",
                    "With my mom",
                    "With my wife"
                ],
                "answer": "With my mom"
            },
            {
                "question": "Who did mom and I see outdoors?",
                "options": [
                    "We saw a hungry little girl",
                    "We Waw a boy selling a cat",
                    "We saw my old friend",
                    "We saw a boy selling drinks"
                ],
                "answer": "We saw a boy selling drinks"
            },
        ]
        
        test_2 = [
            {
                "question": "Who would I go for a walk outside on a hot day?",
                "options": [
                    "With my friend",
                    "With my brother",
                    "With my mom",
                    "With my wife"
                ],
                "answer": "With my mom"
            },
            {
                "question": "Who did mom and I see outdoors?",
                "options": [
                    "We saw a hungry little girl",
                    "We Waw a boy selling a cat",
                    "We saw my old friend",
                    "We saw a boy selling drinks"
                ],
                "answer": "We saw a boy selling drinks"
            },
        ]
        data = [
            test_1,
            test_2,
        ]
        return Response(data)