import requests
info = requests.get("https://pastebin.com/raw/NGsTFapN")
username = input("Enter your username: ")
password = input("Enter your pass: ")
if username and password in info.text:
    print("Do What Ever You Want")
# code code code
else:
    print("Invalid Login Info")
 
