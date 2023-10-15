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
        target = Target(
            name=data["name"],
            attack_priority=data["attack_priority"],
            longitude=data["longitude"],
            latitude=data["latitude"],
            enemy_organization=data["enemy_organization"],
            target_goal=data["target_goal"],
            was_target_destroyed=data["was_target_destroyed"],
            target_id=data["target_id"]
        )
        serializer = TargetSerializer(data=data)
        if serializer.is_valid():
            target.save()
            return JsonResponse({"message": "Target created successfully"})
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
                target.name= request_data['name']
                target.attack_priority = request_data["attack_priority"]
                target.longitude = request_data["longitude"]
                target.latitude = request_data['latitude']
                target.enemy_organization = request_data["enemy_organization"]
                target.target_goal = request_data["target_goal"]
                target.was_target_destroyed = request_data["was_target_destroyed"]
                target.save()
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
