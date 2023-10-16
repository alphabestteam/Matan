from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
import json

from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def add_target(request):
    # Implement here an add function
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        target = TargetSerializer(data)
        serializer = TargetSerializer(data=data)
        if serializer.is_valid():
            target.save()
            return JsonResponse({"message": "Target created successfully"}, status=200)
        else:
            return JsonResponse({"message": "Invalid request method"}, status=400)

@csrf_exempt
def update_target(request):
    # Implement here an update function
  if request.method == 'PUT':
        try:
            request_data = JSONParser().parse(request)
            pk = request_data.get('target_id', None)
            target = Target.objects.get(target_id=pk)
            serializer = TargetSerializer(target, data=request_data)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            
            return JsonResponse(serializer.errors, status=400)
        except ObjectDoesNotExist:
            # Handle the case where the target does not exist
            return JsonResponse({'error': 'Target not found'}, status=404)


def all_targets(request):
    # Implement here a get all targets function
    if request.method == 'GET':
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return JsonResponse(serializer.data, safe=False)
