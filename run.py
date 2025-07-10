#!/usr/bin/env python3

import os
import requests


image_location= os.path.expanduser("~/supplier-data/descriptions/")
url= "http://[external-IP-address]/fruits"


for filename in os.listdir(image_location):
    fruit_list= ['name','weight', 'description', 'image_name']
    listFruitDescription =[]
    with open(image_location+filename,'r')as file:
        for line in file:
            print(line.strip())
            listFruitDescription.append(line.strip())
            
    fruit_dict= dict(zip(fruit_list,listFruitDescription))
    fruit_dict['image_name']=filename[0:3]+'jpeg'
    fruit_dict['weight']=int(fruit_dict['weight'])
    response = requests.post(url,json=fruit_dict)
    if response.status_code== 200:
        print("POST request successful (Status Code 200 OK)")
    elif response.status_code == 201:
        print("POST request successful (Status Code 201 Created)")
    else:
        print(f"POST request failed with status code: {response.status_code}")
        print(response.request.body)
       
    
            
            