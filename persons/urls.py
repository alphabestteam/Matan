"""
URL configuration for persons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from person.views import get_all_people, add_person, delete_person, update_person, add_parent, connect_kid, view_parent, rich_kids, get_parents_of_person, get_kids, get_grandparents, qset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getAllPeople', get_all_people, name='getAllPeople'),
    path('api/addPerson/', add_person, name='addPerson'),
    path('api/removePerson/<int:id>/', delete_person, name='removePerson'),
    path('api/updatePerson/', update_person, name='updatePerson'),
    path('api/addParent/', add_parent, name='addParent'),
    path('api/connectKid/', connect_kid, name='connectParent'),
    path('api/viewParent/<int:id>/', view_parent, name='viewParent'),
    path('api/richKids/', rich_kids, name='richKids'),
    path('api/parentFinder/<int:id>/', get_parents_of_person, name='parentFinder'),
    path('api/kidFinder/<int:id>/', get_kids, name='kidFinder'),
    path('api/grandparentFinder/<int:id>/', get_grandparents, name='get_grandparents'),
    path('api/qset/<int:num>/', qset, name='qset'),
]
 