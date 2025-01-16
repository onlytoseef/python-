# string operation 

chai = "Lemon Tea"
# slicing in string 
slice_chai = chai[0:5]
print(slice_chai)
negative_chai = chai[-1]
print(negative_chai)

num_list = "0123456789"
num_list = num_list[:7]
print(num_list)


chot = chai.lower()
print(chot)
print(chai)

# removing spaces 
masla = "   chai   "
masla.strip()

# converting string to list
members = "Toseef,Tayyab,Umar,Zohaib"
print(members.split())

# finding a word in string
search = "TOseef rana bhai"
print(search.find("rana"))

# finding count number of any word in string 

random = "Ary bhaiya  bhaiya bhaiya bhaiya kidhr ja rhy ho "
print(random.count("bhaiya"))

# passing variables in string (Placeholder)

quantity = 5
chai = "Lemon Tea"
order = "I ordered {} cups of {}"
print(order.format(quantity,chai))

# creating string from list
chai_variety = ["Lemon Tea","Ginger Tea","Masla Tea"]
chai_string =  ", ".join(chai_variety)
print(chai_string)

# finding length of string
length_chai = len(chai)
print(length_chai)

# printing raw sting 

path = "chai:\\user\nlocaldisk"
print(path)

# raw string
path = r"chai:\\user\nlocaldisk"
print(path)