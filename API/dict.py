dict = {
    'name' : 'Ashish',
    'gender' : 'male',
    'age' : 26,
    'sub' : {
        'dsa' : 50,
        'maths' : 67,
        'english' : 34
    }
}

#Accessing 2D dict
# print(dict['sub']['dsa'])

#POP
# dict.pop('age')

#Get
# print(dict.get('name'))

# del
# del dict['name']
# print(dict)

#Dict Operations
# for i in dict :
    # print(i)  # print only key 
    # print(i,dict[i]) # print key value pair


###### Dictionary Comprehension ######

#Print 1st 10 numbers and their squares
# d={i:i**2 for i in range (1,11)}
# print(d)

# Using existing dict (change KM to Miles)

# distances = {
#     'delhi' : 1000,
#     'mumbai' : 2300,
#     'goa' : 2500,
#     'patna' : 300    
# }

# dis_miles = {i:j*0.62 for (i,j) in distances.items()}
# print(dis_miles)