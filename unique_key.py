import json
dictionary={"a": 1,"a": 2, "a": 3,"a": 4,"b": 1,"b": 2}
unique={}
for i in dictionary:
    if i not in unique:
       unique[i]=dictionary[i]
#print(unique) 
with open("unique key_value","w") as file:
    json.dump(dictionary,file)
