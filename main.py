import os
from User import User
from time import ctime
from sys import getsizeof
import json
from pathlib import Path



print("if you want to change username then input 'change_username'")
data = Path("User.json").read_text()
user = json.loads(data)
dede = user[0]["Username"]

while True:
    def cd():
        try:
            p_ath = input("input path>>")
            print(p_ath)
            os.chdir(p_ath)
        except FileNotFoundError:
            print("file not found")

    user = input(dede + ">>")

    def py():
        print("hello")

    def change_dir():
        try:
            p_ath = input("input path>>")
            os.chdir(p_ath)
        except FileNotFoundError:
            print("file not found")

    def help__():
        print(""""
                  cd        changes the current working directory to the specified path.
                  open      opens a directory or file.
                  mkdir     creates any intermediate directories in the path, if needed.
                  py        Nothing
                  Tree      it list the specified directory
                  change_user changes user""")

    def open_file():
        try:
            directory = input("file>> ")
            os.startfile(directory)
        except FileNotFoundError or FileExistsError:
            print("File Not found")
        else:
            print("file opening...")
            print("file opened")

    def mk_dir():
        try:
            print("input directory")
            direct = input("file>>")
            os.mkdir(direct)
        except FileExistsError:
            print("failed to create file")
            print("file already exists")

    def lst_dir():
        path = input("enter directory>>")
        print(path)
        for root, dirs, files in os.walk(path):
            for f in files:
                print(os.path.join(root, f))
                print("size of files>", getsizeof(root), "bytes")





    def time():
        print(ctime())


    def change_user():
        name = input("Username:")

        user_data = [
            {"Username": name}
        ]
        data = json.dumps(user_data)
        Path("User.json").write_text(data)

        print("Rerun app")

    if user.lower() == "cd":
        change_dir()
    if user.lower() == "help":
        help__()
    elif user.lower() == "time":
        time()
    elif user.lower() == "open":
        open_file()
    elif user.lower() == "tree":
        lst_dir()
    elif user.lower() == "py":
        py()
    elif user.lower() == "quit" or user.lower == "exit":
        print("good bye..")
        break
    elif user == "" or user == " ":
        pass
    elif user.lower() == "mkdir":
        mk_dir()
    elif user.lower() == "change_username":
        change_user()
    else:
        print("'", user, "'", "is not recognized as an internal or external command,operable program or batch file.")
