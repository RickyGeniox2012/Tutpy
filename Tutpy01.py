# Tutpy01
# First tutorial. Using variables and print()

name="Ricky"
surname="Genio"
full_name=name+" "+surname
age=10
height=140
print (name)
# Output:
#  Ricky

print (name+" "+surname)
# Output:
#  Ricky Genio

print ("Name and Surname: " + name + " " + surname)
# Output:
#  Name and Surname: Ricky Genio

print ("Name: {}" .format(name))
print ("Surname: {}". format(surname))
# Output:
# Name: Ricky
# Surname: Genio

print (f"Name: {name}, Surname: {surname}")
# Output:
#  Name: Ricky, Surname: Genio

print ("Your name is %s, and your surname is %s" % (name, surname))
# Output:
# Your name is Ricky,
# and your surname is Genio

print ("Your height is: "+str(height)+"cm")
# Output:
# Your height is: 140cm

kid = True
print ("Are you a kid: "+str(kid))
# Output:
# Are you a kid: True