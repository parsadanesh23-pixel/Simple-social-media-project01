class menu1:
    def __init__(self,username):
        self.username=username
    def main_menu(self):
        import json
        with open("posts.json","r") as file:
            posts=json.load(file)
        while True:
            try:
                menu=int(input("""1. post a note
                2. see the posts of a person
                3. see the posts of yourself
                4. delete your post
                5. see the every posts
                6. exit
                enter number: """))
            except ValueError:
                print("enter number")
            else:
                if menu==1:
                    write1=input("write your post: ")                
                    if self.username not in posts:
                        posts[self.username]={}

                    while True:
                        questadd1=input("if you like to add your post type , and not, type 2: ")
                        if questadd1!="2":
                            posts[self.username][write1]={"name":self.username
                            }
                            with open("posts.json","w") as file:
                                json.dump(posts,file,indent=4)
                            break
                        elif questadd1=="2":
                            print("your note has not been posted")
                            break
                elif menu==2:
                        questsee1=input("gave the username of your selected user: ")
                        if questsee1 in posts:
                            for things in posts[questsee1]:
                                print(f"name: {questsee1} / {posts[questsee1][things]}")
                        else:
                            print("invalid username")
                elif menu==3:
                    if posts[self.username]!=[]:
                        print(posts[self.username])
                    else:
                        print("there is no post")
                elif menu==4:
                    message=input("gave the exact text of what you want to delete: ")
                    if message in posts[self.username]:
                        del posts[self.username][message]
                        with open("posts.json","w") as file:
                            json.dump(posts,file,indent=4)
                        print("done !")
                    else:
                        print("there is no message like this")
                elif menu==5:
                    for things in posts:
                        print(posts[things])
                elif menu==6:
                    break