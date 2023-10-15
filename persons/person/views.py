from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer


@api_view(['GET'])
def get_all_people(request):
    """
    function that returns all of the people in the db
    """
    arr = []
    for item in Person.objects.all():
        arr += PersonSerializer(item)
        print(arr)

    return HttpResponse(arr, status=200)


