import requests
info = requests.get("https://pastebin.com/raw/yoururl") # Accessing The Pasebin link...
username = input("Enter your username: ") # Username Input
password = input("Enter your pass: ") # Password Input
if username and password in info.text: # Checks if the user inputs are in the pastebin 
    print("Do What Ever You Want") # If the user inputs are correct do 'code code code'
# code code code
else: # if the user credentials are wrong do 'code code code'
    print("Invalid Login Info")
 
