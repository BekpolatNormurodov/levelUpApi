from rest_framework.response import Response
from rest_framework.views import APIView

class Conversation(APIView):
    def get(self, request):
        conversation_1 =  {
            "title": ["Jeffrey","Daniel"],
            "person-1": {
                "text_en": [
                    "Hello, are you Jeffrey?",
                    "Hi Daniel. My name is Marina Garcia. How are you?",
                    "it's nice to meet you, too. Where is your brother?",
                    "How old are you?",
                    "Where are you from?"
                ],
                "text_uz": [
                    "Salom, siz Jeffrimisiz?",
                    "Salom Daniel. Mening ismim Marina Garsiya. Qalaysiz?",
                    "siz bilan ham tanishganimdan xursandman. Ukangiz qayerda?",
                    "Yoshingiz nechida?",
                    "Qayerliksiz?"
                ]
            },
            "person-2": {
                "text_en": [
                    "No, I'm not. My name is Daniel. Jeffrey is my Brother",
                    "I'm fine. it's nice to meet you, Marina.",
                    "He is at work.",
                    "I am 25 years old.",
                    "I am from Santo Domingo"
                ],
                "text_uz": [
                    "Yo'q, men emasman. Mening ismim Daniel. Jeffri mening akam",
                    "Men yaxshiman. Siz bilan tanishganimdan xursandman, Marina.",
                    "U ishda.",
                    "Men 25 yoshdaman.",
                    "Men Santo-Domingodanman"
                ]
            },
        },
        conversation_2 =  {
             "title": ["Jeffrey","Daniel"],
            "person-1": {
                "text_en": [
                    "Hello, are you Jeffrey?",
                    "Hi Daniel. My name is Marina Garcia. How are you?",
                    "it's nice to meet you, too. Where is your brother?",
                    "How old are you?",
                    "Where are you from?"
                ],
                "text_uz": [
                    "Salom, siz Jeffrimisiz?",
                    "Salom Daniel. Mening ismim Marina Garsiya. Qalaysiz?",
                    "siz bilan ham tanishganimdan xursandman. Ukangiz qayerda?",
                    "Yoshingiz nechida?",
                    "Qayerliksiz?"
                ]
            },
            "person-2": {
                "text_en": [
                    "No, I'm not. My name is Daniel. Jeffrey is my Brother",
                    "I'm fine. it's nice to meet you, Marina.",
                    "He is at work.",
                    "I am 25 years old.",
                    "I am from Santo Domingo"
                ],
                "text_uz": [
                    "Yo'q, men emasman. Mening ismim Daniel. Jeffri mening akam",
                    "Men yaxshiman. Siz bilan tanishganimdan xursandman, Marina.",
                    "U ishda.",
                    "Men 25 yoshdaman.",
                    "Men Santo-Domingodanman"
                ]
            },
        },
        
        data = [
            conversation_1, 
            conversation_2,
        ]
        return Response(data)