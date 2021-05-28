import requests
codes = requests.get("https://pastebin.com/yoururl")
username = input("Enter your username: ")
password = input("Enter your pass: ")
if username and password in codes.text:
# Do anything you want 
 
