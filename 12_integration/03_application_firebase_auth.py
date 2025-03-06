import pyrebase

firebaseConfig = {
    "apiKey" : "AIzaSyBzPRzWQ986l6ZT4uAa4YKH-e7GngHrDN0",
    "authDomain" : "authpython-ae723.firebaseapp.com",
    "projectId" : "authpython-ae723",
    "storageBucket" : "authpython-ae723.appspot.com",
    "messagingSenderId" : "306339829215",
    "appId" : "1:306339829215:web:1bd23e4610205305c4606a",
    "databaseURL" : "https://authpython-ae723-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def signUp():
    email = input("email: ")
    password = input("password: ")

    auth.create_user_with_email_and_password(email, password)
    print("created user")

def login():
    email = input("email: ")
    password = input("password: ")

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(user)
        print(auth.get_account_info(user["idToken"]))
        print("login is made")
    except:
        print("invalid email or password")

# signUp()
login()