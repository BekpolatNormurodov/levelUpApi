from rest_framework.response import Response
from rest_framework.views import APIView

class Vocabulary(APIView):
    def get(self, request):
        vocabulary_1 = {"vocabulary_en": ["Bank", "Account", "Deposit", "Loan", "Interest"], "vocabulary_uz": ["Bank", "Hisob", "Depozit / Pul qo`yish", "Kredit / Qarz", "Foiz"], "sentence_en": ["I receive my salary through the bank every month.", "I have enough funds in my bank account.", "He deposited money in the bank to buy a house.", "He took a loan from the bank to buy a new car.", "The interest rate of this bank is very low."], "sentence_uz": ["Men har oy maoshimni bank orqali olaman.", "Mening bank hisobimda yetarlicha mablag` bor.", "U uy sotib olish uchun bankka depozit qo`ydi.", "U yangi mashina sotib olish uchun bankdan kredit oldi.", "Bu bankning kredit foizi juda past ekan."],}
        vocabulary_2 = {"vocabulary_en": ["Bank", "Account", "Deposit", "Loan", "Interest"], "vocabulary_uz": ["Bank", "Hisob", "Depozit / Pul qo`yish", "Kredit / Qarz", "Foiz"], "sentence_en": ["I receive my salary through the bank every month.", "I have enough funds in my bank account.", "He deposited money in the bank to buy a house.", "He took a loan from the bank to buy a new car.", "The interest rate of this bank is very low."], "sentence_uz": ["Men har oy maoshimni bank orqali olaman.", "Mening bank hisobimda yetarlicha mablag` bor.", "U uy sotib olish uchun bankka depozit qo`ydi.", "U yangi mashina sotib olish uchun bankdan kredit oldi.", "Bu bankning kredit foizi juda past ekan."],}

        data = [
            vocabulary_1,
            vocabulary_2,
        ]
        return Response(data)