import json
class start:
    def __init__(self,username,name,password):
        self.name=name
        self.username=username
        self.password=password
    def signup(self):
        with open("users.json","r") as file:
            userdata=json.load(file)
        userdata[self.username]={"username":self.username,
        "name":self.name,
        "password":self.password
        }
        with open("users.json","w") as file:
            json.dump(userdata,file,indent=4)