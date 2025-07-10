import reports
import email
import os
from datetime import date





image_location= os.path.expanduser("~/supplier-data/descriptions/")
url= "http://[external-IP-address]/fruits"


def get_fruit_info():
    fruit_n_weight=[]
    for filename in os.listdir(image_location):
        fruit_list= ['name','weight', 'description']
        listFruitDescription =[]
        with open(image_location+filename,'r')as file:
            for line in file:
                print(line.strip())
                listFruitDescription.append(line.strip())
            
        fruit_dict= dict(zip(fruit_list,listFruitDescription))
        fruit_dict['weight']=int(fruit_dict['weight'])
        fruit_holder= {'name':fruit_dict['name'], 'weight':fruit_dict['weight']}
        fruit_n_weight.append(fruit_holder)
    return fruit_n_weight

def processdata(fruit_name_n_weight):
    starting_string = ''
    for name, weight in fruit_name_n_weight:
        starting_string += f"name: {name}\nweight: {weight} lbs\n\n"
    return starting_string



if __name__ == "__main__":
    today= str(date.today())
    title = "Processed Update on "+ today
    allfruit= processdata(get_fruit_info())
    reports.generate_report("/tmp/processed.pdf",title, allfruit)
    
    sender= "automation@example.com"
    recipient= "student@example.com"
    subject= "Upload Completed - Online Fruit Store"
    
    body= "\n".join("All fruits are uploaded to our website successfully. A detailed list is attached to this email.")
    message = email.generate(sender, recipient, subject, body,"/tmp/processed.pdf")
    email.send(message)
    