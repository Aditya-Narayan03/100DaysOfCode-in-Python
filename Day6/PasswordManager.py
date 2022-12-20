
print("\nUsage :\n\
- MASTER PASSWORD will be used to encrypt your password and then safely store them.\n\
- To see already existing passwords, type 'view'.\n\
- To add new passwords, type 'add'.\n\
- And to quit the process, press 'Quit'\n\
------------------------------------------------------------------------------------------\n")

master_passwd = input("Please enter MASTER PASSWORD : ")


def add():
    print("-------------------------------------------")
    print("\nStarting the ADD Operations....\n")
    username = input("Enter your username : ").lower()
    password = input("Enter your password : ").lower()

    with open("passwords.txt", 'a') as f:
        f.write(username + ":" + password + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f:

            myData = line.rstrip("\n")
            usernm, pswd = myData.split(":")
            print(usernm + ' : ' + pswd)


while True:
    mode = input("View, Add or Quit : ").lower()

    if mode == 'quit':
        print("Quitting the process as per request.......")
        break

    if mode == 'view':
        view()

    elif mode == 'add':
        add()

    else:
        print("---------------------------------------------")
        print('\nINVALID ARGUMENT!!!\nQuiting the process....')
        break