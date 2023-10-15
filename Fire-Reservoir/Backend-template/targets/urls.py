from django.urls import path
from . import views

urlpatterns = [
    # Add here all the URLs you need
    path("AddTarget/", views.add_target),
    path("AllTargets/", views.all_targets),
    path("UpdateTarget/", views.update_target),
]
