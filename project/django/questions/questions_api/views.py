from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import AnswersSerializer, QuestionsSerializer
from rest_framework.response import Response
from .models import Questions, Answers
from rest_framework.generics import get_object_or_404
from rest_framework import status


class QuestionsListApiView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    
class QuestionsCreateApiView(generics.CreateAPIView):
    serializer_class = QuestionsSerializer
    permission_classes=[IsAuthenticated]
    
class AnswersOfQListApiView(generics.ListAPIView):
    serializer_class = AnswersSerializer
    
    def get_queryset(self):
        return Answers.objects.filter(questions_id=self.kwargs.get('id'))

class QuestionsDeleteApiView(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    
    def delete(self, **kwargs):
        object = get_object_or_404(Questions, id=kwargs.get('id'))
        object.delete()
        return Response({'detail':'question deleted'}, status=status.HTTP_200_OK)
    

class AnswerRDApiView(generics.RetrieveDestroyAPIView):
    serializer_class = AnswersSerializer
    permission_classes=[IsAuthenticated]
    
    def get_object(self):
        object = Answers.objects.get(pk=self.kwargs.get('id'), user_id=self.request.user)
        return object
    
class AnswerCreateApiView(generics.CreateAPIView):
    serializer_class = AnswersSerializer
    
    def post(self, request, **kwargs):
        data = request.data
        print(data)
        q_id = kwargs.get('id')
        serial = self.get_serializer(data=data, context={'question_id': q_id, 'user_id': self.request.user})
        
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response(serial.data, status=status.HTTP_201_CREATED)
    