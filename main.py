import re

def reg():
    reg_email = input("Enter your email ID")
    regex = r'\b[^0-9!@#$%^&*][A-Za-z0-9.x]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if (re.fullmatch(regex, reg_email)):
        print("Valid Email")
        flag = 0
        passwd = input("Enter your password")



        if not re.search('[a-z]', passwd):
            flag = 1
        if not re.search('[0-9]',passwd):
            flag=1
        if not re.search('[A-Z]',passwd):
            flag=1
        if not re.search('[&%$#@!*]',passwd):
            flag = 1
        if not len(passwd)>5 and len(passwd)<16 :
            flag = 1

        if flag==0:
            print("Valid Password")
            f = open("db.txt", "a")
            f.write(reg_email+", "+passwd+"\n")
            print("Successfully Registered")


        else:
            print("Invalid password")
            reg()
    else:
        print("Invalid Email")
        reg()

def login():
    f = open("db.txt", "r")
    Username = input("Enter Username")
    u = []
    p = []
    for i in f:
        a, b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u, p))
    if Username in data:
        Password = input("Enter Password")
        if data[Username] == Password:
            print("Welcome")

        else:
            print("Password Incorrect")
            print("Forgot Password")
            fp = int(input("Press 1 to know your original password"))
            if fp == 1:
                w = data.get(Username)
                print(w)


    else:
        print("Your Mail ID is not Registered, Please Register")
        home()



def home():
    choose = int(input("Choose 1. For Login or 2. For Register "))
    if choose == 1:
        login()
    elif choose == 2:
        reg()
    else:
        print("Select Correct Option")
        home()


home()






















