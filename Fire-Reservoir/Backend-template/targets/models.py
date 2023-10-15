from django.db import models

class Target(models.Model):
    # Implement here a target model with a __str__ function
    name = models.CharField(max_length=255)
    attack_priority = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    enemy_organization = models.CharField(max_length=255)
    target_goal = models.CharField(max_length=255)
    was_target_destroyed = models.BooleanField()
    target_id = models.IntegerField(primary_key=True)