from rest_framework.response import Response
from rest_framework.views import APIView
    
class conversationTest1(APIView):
    def get(self, request):
        test_1 = [
            {
                "question": "Hello, are you Jeffrey?",
                "options": [
                    "No, I'm not. My name is Daniel. Jeffrey is my Brother",
                    "I'm fine. it's nice to meet you, Marina.",
                    "He is at work.",
                    "I am 25 years old."
                ],
                "answer": "No, I'm not. My name is Daniel. Jeffrey is my Brother"
            },
            {
                "question": "Hi Daniel. My name is Marina Garcia. How are you?",
                "options": [
                    "No, I'm not. My name is Daniel. Jeffrey is my Brother",
                    "I'm fine. it's nice to meet you, Marina.",
                    "He is at work.",
                    "I am 25 years old."
                ],
                "answer": "I'm fine. it's nice to meet you, Marina."
            }
        ]
        
        test_2 = [
            {
                "question": "Hello, are you Jeffrey?",
                "options": [
                    "No, I'm not. My name is Daniel. Jeffrey is my Brother",
                    "I'm fine. it's nice to meet you, Marina.",
                    "He is at work.",
                    "I am 25 years old."
                ],
                "answer": "No, I'm not. My name is Daniel. Jeffrey is my Brother"
            },
            {
                "question": "Hi Daniel. My name is Marina Garcia. How are you?",
                "options": [
                    "No, I'm not. My name is Daniel. Jeffrey is my Brother",
                    "I'm fine. it's nice to meet you, Marina.",
                    "He is at work.",
                    "I am 25 years old."
                ],
                "answer": "I'm fine. it's nice to meet you, Marina."
            }
        ]
        data = [
            test_1,
            test_2,
        ]
        return Response(data)