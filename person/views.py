from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Person, Parent
from .serializers import PersonSerializer, ParentSerializer, ConnectKidSerializer
import json
from django.db.models import Q, Avg, Count, Max, Sum


@api_view(["GET"])
def get_all_people(request):
    """
    function that returns all of the people in the db§
    time:  0.010687828063964844
    query_count:  1
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
    time:  0.014688968658447266
    query_count:  1
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
    time:  0.0043108463287353516
    query_count:  1
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
    time:  0.00690007209777832
    query_count:  1
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
    time:  0.006392002105712891
    query_count:  1
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
    time:  0.0043108463287353516
    query_count:  1
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
    """
    time:  0.008362293243408203
    query_count:  1
    """
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
    time:  0.006682872772216797
    query_count:  1
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
    time:  0.004760026931762695
    query_count:  1
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
    """ 
    time:  0.0038299560546875
    query_count:  1
    """
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
    """
    time:  0.012375116348266602
    query_count:  1
    """
    try:
        parent = Parent.objects.get(id=id)
    except Parent.DoesNotExist:
        return Response({"error": "Parent not found"}, status=404)

    kids = parent.kids.all()
    serializer = PersonSerializer(kids, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_grandparents(request, id):
    """
    time:  0.004119157791137695
    query_count:  1
    """
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
    """
    time:  0.004249157791137695
    query_count:  1
    """
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)
    
    parents = person.parents.all()
    brothers = []

    for parent in parents:
        brothers.extend(parent.kids.all())

    serializer = PersonSerializer(brothers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def qset(request, num):

    if num == 1:
        parents_info = Parent.objects.values('name', 'date_of_birth', 'city', 'work_place', 'salary')   
        for parent in parents_info:
            print(parent)

    if num == 2:
        query_set = Parent.objects.filter(work_place = "Google")
        count = query_set.count()
        print(count)

    if num == 3:
        query_set = Parent.objects.filter(name = "Roee")[0]
        kids = query_set.kids.all().values('name', 'date_of_birth', 'city')
        print(kids)

    if num == 4:
        query_set = Person.objects.filter(Q(name__icontains = "i")).values('name', 'date_of_birth', 'city')
        print(query_set)

    if num == 5:
        query_set = Person.objects.filter(city__in=["Raanana", "Tel Aviv"]).values('name', 'date_of_birth', 'city')
        print(query_set)

    if num == 6:
        average_salary = Parent.objects.aggregate(avg_salary=Avg('salary'))
        print(average_salary)

    if num == 7:
        parents_with_children_count = Parent.objects.annotate(
        children_count=Count('kids')).values('name', 'children_count')

        for parent in parents_with_children_count:
            print(parent)

    if num == 8:
        total_kids = Parent.objects.aggregate(total_kids=Count('kids'))
        print(total_kids)

    if num == 9:
        richest_parent = Parent.objects.aggregate(max_salary=Max('salary'))
        max_salary = richest_parent['max_salary']
        richest_parents = Parent.objects.filter(salary=max_salary)
        richest_parent = richest_parents.first()

        print(richest_parent.name, richest_parent.salary)

    
    if num == 10:
        kids = Person.objects.filter(parents__salary__gt=0)
        kids = kids.annotate(total_parent_salary=Sum('parents__salary'))
        kids = kids.filter(total_parent_salary__gt=50000)

        for kid in kids:
            print(kid.name, kid.city)


    return Response(status=200)


