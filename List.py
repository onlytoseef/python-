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

