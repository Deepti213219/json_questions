# Q.3 Python object ko json string mai convert karne ka program likho?

import json
dic = {"name":"deepti","class":"12th","school":"vidya & child"}
file2=open("json_file1.json","w")
json.dump(dic,file2,indent=4)

file2.close()
