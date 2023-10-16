from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
import json


@api_view(["GET"])
def get_all_people(request):
    """
    function that returns all of the people in the db
    """
    arr = []
    for item in Person.objects.all():
        serializer = PersonSerializer(item)
        arr.append(serializer.data)
    return Response(arr, status=200)


@api_view(["POST"])
@parser_classes([JSONParser])
def add_person(request):
    """
    This function adds a person to db or updates it
    """
    data = json.loads(request.body.decode("utf-8"))
    try:
        person = Person.objects.get(id=data["id"])
    except Person.DoesNotExist:
        # Handle the case where the person does not exist
        person = None

    if not person:
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)
    else:
        serializer = PersonSerializer(person, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)


@api_view(["POST"])
def delete_person(request, id):
    """
    this function deletes Person from db
    """
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        # Handle the case where the person does not exist
        person = None

    if person:
        person.delete()
        return Response(status=200)
    else:
        return Response("person not found", status=400)


@api_view(["POST"])
@parser_classes([JSONParser])
def update_person(request):
    """
    This function update persons
    """
    data = json.loads(request.body.decode("utf-8"))
    try:
        person = Person.objects.get(id=data["id"])
    except Person.DoesNotExist:
        # Handle the case where the person does not exist
        person = None


    if person:
        serializer = PersonSerializer(person, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response("person isn't found", status=400)
    
