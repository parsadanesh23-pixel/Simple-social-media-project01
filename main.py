import json
from menu import menu1
from user import start


with open("users.json","r") as file:
    userdata=json.load(file)


def wrong():
    print("there is something wrong")


def enter_number():
    print("enter number !")        

while True:
    try:
        quest=int(input("""1. sign up (i am new)
        2. login
        3. exit
        enter number: """))
    except ValueError:
        enter_number()
    else:
        if quest==1:
            username1=input("gave your username: ")
            if username1 in userdata:
                wrong()
            else:
                while True:
                    password1=input("""gave your password:
                    type 0 to go back
                    number of chars in your password should be 8 or more
                    type: """)
                    if len(password1)<8:
                        print("try again")
                    elif password1=="0":
                        break
                    else:
                        name=input("gave your name: ")
                        start(username1,name,password1).signup()
                        menu1(username1).main_menu()

        elif quest==2:
            username2=input("gave your username: ")
            password2=input("gave your password: ")
            if username2 in userdata:
                if password2==userdata[username2]["password"]:
                    print("welcome !")
                    menu1(username2).main_menu()
                else:
                    wrong()
            else:
                wrong()
        elif quest==3:
            print("good luck")
            break
