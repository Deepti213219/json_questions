# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho? 
import json
dic = {'4': 5, '6': 7,'1': 3,'2': 4}
list1=[]
for i in dic:
   list1.append(i)
#print(list1)
i=0
while i<len(list1):
    j=0
    while j<len(list1):
        if list1[i]<list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
        j=j+1
    i=i+1
#print(list1)
x=0
dic1={}
while x<len(list1):
    dic1[list1[x]]=dic[list1[x]]
    x+=1
#print(dic1)

with open("sorting.json","w") as file:
     json.dump(dic1,file,indent=3)
        