import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","2000"]
list3=["anuradha","HR","24","40000"]
list4=["Abhishek","manager","29","63000"]  

a=["name","destination","age","salary"]
dic1={}
dic2={}
dic3={}
dic4={}
dictionary={}
i=0
while i<len(a):
    j=0
    while j<len(a):
        dic1[a[i]]=list1[j]
        dic2[a[i]]=list2[j]
        dic3[a[i]]=list3[j]
        dic4[a[i]]=list4[j]
        j=j+1
        dictionary["emp1"]=dic1
        dictionary["emp2"]=dic2
        dictionary["emp3"]=dic3
        dictionary["emp4"]=dic4
        i=i+1

# print(dictionary)

with open("employe_details.json","w") as f:
    json.dump(dictionary,f,indent=4)