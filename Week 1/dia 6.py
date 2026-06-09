#def happy_birthday(name, age):
    #print(f"happy birth day to {name}")
    #print(f"you are {age} years old")
    #print("happy birthday to you!")
    #print()

#happy_birthday("bro", 20)
#happy_birthday("steve", 34)
#happy_birthday("bro", 45)

#def display_invoice(username, amount, due_date):
    #print(f"hello {username}")
    #print(f"your bill of ${amount:.2f} is due: {due_date} ")

#display_invoice("reyes", 20000, "01/02/2030")

#def add(x, y):
  #  z = x + y
 #   return z
#def subtract(x, y):
  #  z = x - y
 #def multiply(x, y):
  #  z = x * y
 #   return z
#def divide(x, y):
    #z = x / y
    #return z
#print(add(2, 3))
#print(subtract(2, 3))
#print(multiply(2, 3))
#print(divide(2, 3))

#def create_name(first_name, last_name):
    #first_name = first_name.capitalize()
    #last_name = last_name.capitalize()
    #return f"{first_name} {last_name}"
#first_name = input("Enter first name: ")
#last_name = input("Enter last name: ")
#print(create_name(first_name, last_name))

def gc_content(seq):
    gc = seq.count("GC")
    return (gc)
result = gc_content("ATGchat,CGCG")
print(result)