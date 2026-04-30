Names=[]

with open ("customers.txt","r") as file:
    for line in file:
        Name = line.split(",")[1]
        if Name == "Name":
            continue
        else:
            Proper_name = Name.title()
            Names.append(Proper_name)


print(Names)  
