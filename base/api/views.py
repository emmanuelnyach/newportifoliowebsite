from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Question
from .serializers import QuestionSerializer


@api_view(['GET'])
def votingData(request):
    questions = Question.objects.all()

    seo_content = Question.objects.filter(answer='seo_content').count()
    content_writer = Question.objects.filter(answer='content_writer').count()
    copywriter = Question.objects.filter(answer='copywriter').count()
    #serializer = QuestionSerializer(questions, many=True)

    return Response({'seo_content': seo_content, 'content_writer': content_writer, 'copywriter': copywriter})
