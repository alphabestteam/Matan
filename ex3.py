import pymongo
import json


def main():
    connection_string = "127.0.0.1:27017"
    client = pymongo.MongoClient(connection_string)

    mydb = client["Aviv's_people"]
    family_col = mydb["family"]
    friends_col = mydb["friends"]
    army_col = mydb["army"]

    # query1
    query1 = army_col.find_one({"age": {"$lt": 23}, "role": "DevOps"})
    found_age = query1["age"]
    found_role = query1["role"]

    for i in query1:
        print(i)

    # 2
    query2 = army_col.find_one({"age": found_age, "role": {"$ne": found_role}})
    desired_role = query2["role"]
    army_col.update_one(
        {"age": found_age, "role": found_role}, {"$set": {"role": desired_role}}
    )

    # 3
    for doc in army_col.find().sort("age"):
        if doc["age"] > 23:
            friends_col.insert_one(doc)
            army_col.delete_one(doc)
        else:
            print(doc)

    # test if working:
    # for doc in friends_col.find():
    #     print(doc)


if __name__ == "__main__":
    main()
