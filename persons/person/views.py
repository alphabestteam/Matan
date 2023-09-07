from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Person, Parent
from .serializers import PersonSerializer, ParentSerializer, ConnectKidSerializer
import json


@api_view(["GET"])
def get_all_people(request):
    """
    function that returns all of the people in the db§
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


@api_view(["POST"])
@parser_classes([JSONParser])
def add_parent(request):
    """
    This function adds a parent to db or updates it
    """
    data = json.loads(request.body.decode("utf-8"))
    try:
        parent = Parent.objects.get(id=data["id"])
    except Parent.DoesNotExist:
        # Handle the case where the person does not exist
        parent = None

    if not parent:
        serializer = ParentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)
    else:
        serializer = ParentSerializer(parent, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)


@api_view(["POST"])
def delete_parent(request, id):
    """
    this function deletes parent from db
    """
    try:
        parent = Parent.objects.get(id=id)
    except Parent.DoesNotExist:
        # Handle the case where the person does not exist
        parent = None

    if parent:
        parent.delete()
        return Response(status=200)
    else:
        return Response("parent not found", status=400)


@api_view(["POST"])
def connect_kid(request):
    data = request.data
    person_id = data.get("person_id")
    parent_id = data.get("parent_id")

    try:
        parent = Parent.objects.get(pk=parent_id)
    except Parent.DoesNotExist:
        return Response({"error": "Parent not found"}, status=404)

    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)
    parent.kids.add(person)

    return Response({"message": "Person connected to parent successfully"}, status=200)


@api_view(["GET"])
def view_parent(request, id):
    """
    this function deletes Person from db
    """
    try:
        parent = Parent.objects.get(id=id)
    except Parent.DoesNotExist:
        # Handle the case where the person does not exist
        parent = None

    if parent:
        parent_json = ParentSerializer(parent)
        return Response(JSONRenderer().render(parent_json.data), status=200)
    else:
        return Response("parent not found", status=400)


@api_view(["GET"])
def rich_kids(request):
    """
    returns all the rich kids
    """
    parents = Parent.objects.filter(salary__gt=50000).prefetch_related("kids")
    kids = []

    for parent in parents:
        for kid in parent.kids.all():
            kid_serialized = PersonSerializer(kid)
            kids.append(kid_serialized.data)

    return Response(kids, status=200)


@api_view(["GET"])
def get_parents_of_person(request, id):
    """ """
    request
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)

    parents = person.parents.all()
    serializer = ParentSerializer(parents, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_parents_of_person2(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)

    parents = person.parents.all()
    serializer = ParentSerializer(parents, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_kids(request, id):
    try:
        parent = Parent.objects.get(id=id)
    except Parent.DoesNotExist:
        return Response({"error": "Parent not found"}, status=404)

    kids = parent.kids.all()
    serializer = PersonSerializer(kids, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_grandparents(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)

    parents = person.parents.all()
    grandparents = []

    for parent in parents:
        grandparents.append(parent.parents.all())

    serializer = PersonSerializer(grandparents, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_brothers(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)
    
    parents = person.parents.all()
    brothers = []

    for parent in parents:
        brothers.append(parent.kids.all())

    serializer = PersonSerializer(brothers, many=True)
    return Response(serializer.data)
