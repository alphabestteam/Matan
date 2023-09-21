

#1 docker pull mongo:latest,  
#  docker run -d -p 27017:27017 --name=mongo-example mongo:latest


import pymongo


def main():
    connection_string = "127.0.0.1:27017"
    client = pymongo.MongoClient(connection_string)

    #creation of db
    mydb = client["Aviv's_people"]
    
    #creation of collections
    family_col = mydb["family"]
    friends_col = mydb["friends"]
    army_col = mydb["army"]

    #insert people in 3 different ways
    army_list = [{"name": "Aviv", "age": 20, "role": "Backend"},
                 {"name": "Lihi", "age": 21, "role": "QA"},
                 {"name": "Gabi", "age": 22, "role": "DevOps"},
                 {"name": "Ori", "age": 23, "role": "Front-end"},
                 {"name": "Ido", "age": 22, "role": "Developer"},
                 {"name": "Yarden", "age": 24, "role": "DevOps"}]
    
    x = army_col.insert_many(army_list)
    print(x.inserted_ids)

    y = friends_col.insert_one({"name": "Amit", "age": 20, "role": "Waiter"})
    y = friends_col.insert_one({"name": "Yonatan", "age": 24, "role": "Doctor"})
    y = friends_col.insert_one({"name": "Noa", "age": 22, "role": "Developer"})
    y = friends_col.insert_one({"name": "Michal", "age": 21, "role": "Baker"})
    print(y.inserted_id)

    family_list = [{"_id": 5, "family_role": "Mother", "age": 45, "role": "Teacher"},
                    {"_id": 6, "family_role": "Father", "age": 46, "role": "Engineer"},
                    {"_id": 7, "family_role": "Brother", "age": 12, "role": "School"},
                    {"_id": 8, "family_role": "Sister", "age": 24, "role": "Student"}]
    
    z = family_col.insert_many(family_list)
    print(z.inserted_ids)

    #delete person
    delete_person = {"name": "Lihi"}
    army_col.delete_one(delete_person)

    for x in friends_col.find():
        print(x)

    for x in army_col.find():
        print(x)

    for x in family_col.find():
        print(x)

if __name__ == "__main__":
    main()
