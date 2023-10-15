from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
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
        target.save()
        return JsonResponse({"message": "Target created successfully"})
    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)

# @csrf_exempt
# def update_target(request):
#     # Implement here an update function

# def all_targets(request):
#     # Implement here a get all targets function
