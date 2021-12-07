#!/usr/bin/env python3
import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print ("Usage: "+ sys.argv[0] + " <url>")
    sys.exit(1)

req = requests.get("https://"+sys.argv[1])
print("\n"+ str(req.headers))

hosty = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+ sys.argv[1]+ " is: " + hosty + "\n")

req_2 = requests.get("https://ipinfo.io/"+ hosty + "/json")
response = json.loads(req_2.text)

print("location: "+response["loc"])
print("Region: "+response["region"])
print("City: "+response["city"])
print("Country: "+response["country"])