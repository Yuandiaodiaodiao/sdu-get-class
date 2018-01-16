import os
import json
file_object = open('texts.txt')
try:
     jsons = file_object.read()
finally:
     file_object.close( )
# jsons=jsons.replace("[","{")
# jsons=jsons.replace("]","}")

jsons=json.loads(jsons)

jsonx=jsons  #["object"]["resultList"]
print(jsonx)
