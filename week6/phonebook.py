from cs50 import get_string

people = {
    "David": "+1241412" ,
    "nik": "+352353223"

}

name = get_string("name: ")
if name in people:
    print(f"Number: {people[name]}")