tea_varities = ["tea","white tea","green tea","sabz tea","pyari tea"]
# destructing
print(tea_varities[1])
# destructing from specific index
print(tea_varities[0:2])
print(tea_varities[1:3])
print(tea_varities[1:10])

# adding values to specific index
tea_varities[1:4] = ["Umar","UmarR"]
print(tea_varities)


tea_varities = ["tea","white tea","green tea","sabz tea","pyari tea"]
print(tea_varities)


# adding with same index 
tea_varities[1:1] = ["Jaranwala","Faisalabad"]
print(tea_varities)
# =>it will add whole array after 0 index

# Adding empty arry to specific index
tea_varities[1:3]= []
print(tea_varities)
# => it will delte that values in list simply it is a list

# for loop in python on list

for tea in tea_varities:
     print(tea)

# this will print all the items with - sign
for tea in tea_varities:
     print(tea,end="-")

# checking if character is present in list or not 

if "yestea" in tea_varities:
  print("yes i am avaialble")


# adding item in last 
tea_varities.append("last tea")
print(tea_varities)

# removing last time in list 
tea_varities.pop()
# => it will remove item from last

# removing item with specific name
tea_varities.remove("tea")
print(tea_varities)
# adding element to specific index
tea_varities.insert(0,"tea")
print(tea_varities)

# creating a deep copy

tea_varities_copy = tea_varities.copy()
tea_varities_copy.append("last in copy")
print(tea_varities_copy)

