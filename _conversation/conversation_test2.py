from rest_framework.response import Response
from rest_framework.views import APIView
    
class ConversationTest2(APIView):
    def get(self, request):
        test_1 = [
             {
                "question": "No, I'm not. My name is Daniel. Jeffrey is my Brother",
                "options": [
                    "Hello, are you Jeffrey?",
                    "Hi Daniel. My name is Marina Garcia. How are you?",
                    "it's nice to meet you, too. Where is your brother?",
                    "How old are you?"
                ],
                "answer": "Hello, are you Jeffrey?"
            },
            {
                "question": "I'm fine. it's nice to meet you, Marina.",
                "options": [
                    "Hello, are you Jeffrey?",
                    "Hi Daniel. My name is Marina Garcia. How are you?",
                    "it's nice to meet you, too. Where is your brother?",
                    "How old are you?"
                ],
                "answer": "Hi Daniel. My name is Marina Garcia. How are you?"
            }
        ]
        
        test_2 = [
            {
                "question": "No, I'm not. My name is Daniel. Jeffrey is my Brother",
                "options": [
                    "Hello, are you Jeffrey?",
                    "Hi Daniel. My name is Marina Garcia. How are you?",
                    "it's nice to meet you, too. Where is your brother?",
                    "How old are you?"
                ],
                "answer": "Hello, are you Jeffrey?"
            },
            {
                "question": "I'm fine. it's nice to meet you, Marina.",
                "options": [
                    "Hello, are you Jeffrey?",
                    "Hi Daniel. My name is Marina Garcia. How are you?",
                    "it's nice to meet you, too. Where is your brother?",
                    "How old are you?"
                ],
                "answer": "Hi Daniel. My name is Marina Garcia. How are you?"
            }
        ]
        data = [
            test_1,
            test_2,
        ]
        return Response(data)