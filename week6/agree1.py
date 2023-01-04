from cs50 import get_string

s = get_string("Do you agree? ")

# or do get_string("Do you agree? ").lower()//

if s.lower() in [ "y", "yes"]:
    print("agreed")
elif s.lower() in [ "n" , "no"]:
    print("dont agree")
else:
    print("say again")