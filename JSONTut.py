import requests
from dotenv import load_dotenv
import json

dumpObj={
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "isEmployed": True,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    },
}
#conversion to json object with dumps where the s is to s(string)
JSONdumpObj = json.dumps(dumpObj, indent=4)
#conversion and dumping in file
with open('person.json',"w") as file:
    json.dump(dumpObj,file, indent=4)
#conversion back to python object with loads where the s is from s(string)
JSONOrignalObj = json.loads(JSONdumpObj)
print(JSONOrignalObj)

with open('person.json' ,"r") as file:
    JSONOrignalObjs = json.load(file)
    print(JSONOrignalObjs)

class User:
    def __init__(self,name,age, city):
        self.name=name
        self.age=age
        self.city=city


user = User("Jane Doe",30,"Chicago")
#encoding custom object
def encode_user(user):
    if isinstance(user,User):
        return {
            "name":user.name,
            "age":user.age,
            "city":user.city,
            user.__class__.__name__:True
        }
    else:
        raise TypeError('wrong ')
    
userJSON=json.dumps(user,default=encode_user)
print(userJSON)

