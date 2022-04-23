import json
data={
    'x':True,
    'y':None,
    'z':False,
}

json_str=json.dumps(data)
print(json_str,data)

with open('dataJs.json','w') as file:
    json.dump(data,file)

with open('dataJs.json','r') as file:
    data=json.load(file)
    print(data)

