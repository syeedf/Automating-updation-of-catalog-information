#!/usr/bin/env python3

import reportlab
import os
import datetime

#processed.pdf

image_location= os.path.expanduser("~/supplier-data/descriptions/")
url= "http://[external-IP-address]/fruits"


for filename in os.listdir(image_location):
    fruit_list= ['name','weight', 'description']
    listFruitDescription =[]
    with open(image_location+filename,'r')as file:
        for line in file:
            print(line.strip())
            listFruitDescription.append(line.strip())
            
    fruit_dict= dict(zip(fruit_list,listFruitDescription))
    fruit_dict['weight']=int(fruit_dict['weight'])


if __name__ == "__main__":


