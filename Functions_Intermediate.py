# 1. Update Values in Dictionaries and Lists
x = [[5,2,3], [10,8,9]]
x[1][0]= 15
print(x)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory.update({'soccer':['Andres','Ronaldo','Rooney']})
print(sports_directory)

z = [{'x': 10, 'y': 20}]
z[0]['y']=30
print(z)

# 2. Iterate Through a List of Dictionaries
students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(list):
    for x in range(0, len(list)):
        for key,val in list[x].items():
            print(key,"-",val)  
iterateDictionary(students)

# 3. Get Values From a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# 1st Part
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        key = some_list[x][key_name]
        print(key)
iterateDictionary2('first_name',students)
# 2nd Part
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        key = some_list[x][key_name]
        print(key)
iterateDictionary2('last_name',students)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key_name in some_dict:
        list=[]
        for key_value in some_dict[key_name]:
            list.append(key_value)
        print(len(list), key_name)
        for a in range(len(list)):
            print(list[a])
printInfo(dojo)
#c