

import json


def main():
    with open("person.json", "r+") as js:
        data = js.read()
        data_format = json.loads(data)
        
        data_format["name"] = "matan"
        data_format["age"] = 19
        data_format["city"] = "haifa"

        js.truncate(0)
        new = json.dumps(data_format)
        print(new)
        js.write(new)


if __name__ ==    "__main__":
    main()