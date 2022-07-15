import json
name={
    "name":"khusboo",
    "age":18,
    "school name":"DAV Inter college mau",
    "from":"up",
    "villege name"
}
num=open("khusboo.json","r")
file1=json.load(num)
print(file1)
file1.close()