from django.test import TestCase, Client
from .models import Person, Parent
from datetime import datetime
from .serializers import ParentSerializer, PersonSerializer
import json
from rest_framework import status


# Create your tests here.
class YourModelTestCase(TestCase):
    def test_age_18(self):
        birthdate_str1 = "1990-05-15"
        birthdate_date1 = datetime.strptime(birthdate_str1, "%Y-%m-%d").date()
        test1 = Person.objects.create(
            name="Test1", date_of_birth=birthdate_date1, city="Haifa"
        )

        birthdate_str2 = "2007-05-15"
        birthdate_date2 = datetime.strptime(birthdate_str2, "%Y-%m-%d").date()
        test2 = Person.objects.create(
            name="Test1", date_of_birth=birthdate_date2, city="Haifa"
        )

        self.assertEqual(test1.is_over_18_method(), True)
        self.assertEqual(test2.is_over_18_method(), False)

    def test_add_parent(self):
        # test that is correct
        data1 = {
            "name": "Papa",
            "id": 215,
            "date_of_birth": "2004-02-15",
            "city": "Haifa",
            "work_place": "hospital",
            "salary": 400000,
        }

        data1_json = json.dumps(data1)
        client1 = Client()
        response1 = client1.post(
            "http://127.0.0.1:8000/api/addParent/",
            data=data1_json,
            content_type="application/json",
        )
        self.assertEqual(response1.status_code, 200)

        # --------------------------------------------
        # test that is wrong because of missing data, (no salary)
        data2 = {
            "name": "fin",
            "id": 216,
            "date_of_birth": "2004-02-15",
            "city": "Haifa",
            "work_place": "hospital",
        }

        data2_json = json.dumps(data2)
        client2 = Client()
        response2 = client2.post(
            "http://127.0.0.1:8000/api/addParent/",
            data=data2_json,
            content_type="application/json",
        )
        self.assertEqual(response2.status_code, 400)

        # ---------------------------------------------

    def test_delete_parent(self):
        # test that should be correct
        birthdate_str1 = "1990-05-15"
        birthdate_date1 = datetime.strptime(birthdate_str1, "%Y-%m-%d").date()
        test1 = Parent.objects.create(
            name="matan",
            id=125,
            date_of_birth=birthdate_date1,
            city="Haifa",
            work_place="Hospital",
            salary=40000,
        )
        client1 = Client()

        response1 = client1.post(
            "http://127.0.0.1:8000/api/deleteParent/125/",
            content_type="application/json",
        )
        self.assertEqual(response1.status_code, 200)
        # ---------------------------------------------
        # test that should be wrong because id isnot correct
        response2 = client1.post(
            "http://127.0.0.1:8000/api/deleteParent/126/",
            content_type="application/json",
        )
        self.assertEqual(response2.status_code, 400)

    def test_connect_parent(self):
        # test that should work
        birthdate_str1 = "1990-05-15"
        birthdate_date1 = datetime.strptime(birthdate_str1, "%Y-%m-%d").date()
        test1 = Parent.objects.create(
            name="matan",
            id=125,
            date_of_birth=birthdate_date1,
            city="Haifa",
            work_place="Hospital",
            salary=40000,
        )
        test2 = Person.objects.create(
            name="a", id=126, date_of_birth=birthdate_date1, city="Haifa"
        )
        client1 = Client()

        data1 = {"parent_id": 125, "person_id": 126}
        data1_json = json.dumps(data1)

        response1 = client1.post(
            "http://127.0.0.1:8000/api/connectKid/",
            data=data1_json,
            content_type="application/json",
        )
        self.assertEqual(response1.status_code, 200)

        # ---------------------------------------------
        # test that should be wrong because id isnot correct

        data2 = {"parent_id": 125, "person_id": 127}
        data2_json = json.dumps(data2)

        response2 = client1.post(
            "http://127.0.0.1:8000/api/connectKid/",
            data=data2_json,
            content_type="application/json",
        )
        self.assertEqual(response2.status_code, 404)
        response_data = json.loads(response2.content.decode())
        self.assertEqual(response_data, {"error": "Person not found"})


    def test_view_parent(self):
        #test that should work
        birthdate_str1 = "1990-05-15"
        birthdate_date1 = datetime.strptime(birthdate_str1, "%Y-%m-%d").date()
        client1 = Client()
        test1 = Parent.objects.create(
            name="matan",
            id=125,
            date_of_birth=birthdate_date1,
            city="Haifa",
            work_place="Hospital",
            salary=40000,
        )

        response1 = client1.get(
            "http://127.0.0.1:8000/api/viewParent/125/",
            content_type="application/json"
        )
        self.assertEqual(response1.status_code, 200)

        # ---------------------------------------------
        # test that should be wrong because id isnot correct

        response2 = client1.get(
            "http://127.0.0.1:8000/api/viewParent/126/",
            content_type="application/json"
        )
        self.assertEqual(response2.status_code, 400)

    
    def test_brothers(self):
        birthdate_str1 = "1990-05-15"
        birthdate_date1 = datetime.strptime(birthdate_str1, "%Y-%m-%d").date()
        yourself = Person.objects.create(name="YourName", id=124, date_of_birth=birthdate_date1, city="Haifa")

        parent1 = Parent.objects.create(name="Parent1", id=125, date_of_birth=birthdate_date1, city="Haifa", work_place="Hospital", salary=40000)
        parent2 = Parent.objects.create(name="Parent2", id=126, date_of_birth=birthdate_date1, city="Haifa", work_place="Hospital", salary=40000)

        sibling1 = Person.objects.create(name="Sibling1", id=127, date_of_birth=birthdate_date1, city="Haifa")
        sibling2 = Person.objects.create(name="Sibling2", id=128, date_of_birth=birthdate_date1, city="Haifa")

        parent1.kids.set([yourself, sibling1])   
        parent2.kids.set([yourself, sibling2])    

        response = self.client.get(f'/api/brotherFinder/{yourself.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = PersonSerializer([sibling1, sibling2], many=True).data
        print(expected_data)
        self.assertEqual(len(response.data) - 2, len(expected_data))
        #-2 is the diffrence in the names
        

