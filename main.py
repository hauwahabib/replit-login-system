print("REPLIT LOGIN SYSTEM.")
print()
def login():
  while True: 
    username = input("What is your username:")
    password = input("What is your password:")
    if username == "Fatimah" and password == "password":
      print("Welcome to REPLIT!")
      break
    else:
      print("Whoops! I don't recognise the username or password, try  again")
      continue
login()