# we mostly uses dictionary in flask when we are dealing with the nonsql db in flask

chai_types = {"toseef":"developer","smw":"singer","amyy":"actor"}

# => extracting value from name
print(chai_types["toseef"])
# => extracting value with key 
print(chai_types.get("smw"))

# chaning value against a key

chai_types["amyy"] = "singer"
print(chai_types)

# => for loop in dictionary 
for key in chai_types:
        print(key)
# it will print the all the keys in the dictionary instead values

# => for loop to print the keys along the values 
for chai in chai_types:
            print(chai,chai_types[chai])
# this will print the keys along their values

# => for loop to print both value and key
for key,value in chai_types.items():
            print(key,value)

# asking for value in dictionary
if "toseef" in chai_types :
            print("yes he is a developer")

# checking length of dictionary 
print(len(chai_types))


# removing item with they key
chai_types.pop("amyy")
print(chai_types)

# removing last one index 
chai_types.popitem()
print(chai_types)


# adding item to dicitony 
chai_types["karana ujla"] = "faltoo "
print(chai_types)

# removing item from memory refrence 
del chai_types["karana ujla"]
print(chai_types)




