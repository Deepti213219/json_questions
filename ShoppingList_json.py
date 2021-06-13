#Q.9 Apki pass ek shopping name ki ek dictionary hai.
# phir main user se poochu ga ki kon sa item khareedna chahte ho.
# uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.
# phir aapka wo number of items json file se remove karna hai.
# Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.

import json
file2=open("shopping_json.json","w")

shopping={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
user=input("you want to buy item...")
items=int(input("enter how many items you want.."))
for i in shopping.keys() :
    for j in shopping[i].items():
        if user==j:
            shopping([i][j].popitem([user]))
        else:
            shopping[i][user]=str(items)
            shopping.update() 
print(shopping)