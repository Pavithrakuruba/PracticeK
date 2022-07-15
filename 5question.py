# Store two values in x and y and swap them.
import json
num={"name":"khusboo",
     "age":21,
     "college":"D.A.V",
     "marks":60,
     "from":"up"
    }
file=open("my_file.json","r+")
# n=json.load(file)
# n=json.load(file)
# file.close() 
# json.dump(num,file,indent=2)
# file.close()
n=json.load(file)
print(n)
file.closed