# Q.2 Python object ko json data main convert karne ka program likho?

#data={"name": "David","class":"I","age": 6} 
import json
data={"name": "Deepa","class":"I","age": 6}
file1=open("json_file.json","w")
json.dump(data,file1,indent=2)

file1.close()


