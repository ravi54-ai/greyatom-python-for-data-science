# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng', 'Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)
# Append the list
new_class.append('Peter warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)
# create a dictionary
courses = {'Math':'65','English':'70','History':'80','French':'70','Science':'60'}
print(courses)
# Create the Dictionary
marks = courses.values() 
print(marks)

total = int(courses['Math']) +int( courses['English']) + int(courses['History'])+int(courses['French'])+int(courses['Science'])
print(total)
# Slice the dict and stores  the all subjects marks in variable

# Store the all the subject in one variable `Total`
Total = total
# Print the total

# Insert percentage formula
percentage = total*100/500
# Print the percentage
print(percentage)



# Create the Dictionary
 
mathematics = {'Geoffrey Hinton':'78','Andrew Ng':'95','Sebastian Raschka':'65','Yoshua Benjio':'50','Hilary Mason':'70','Corinna Cortes':'66','Peter Warden':'75'}

topper = max(mathematics,key= mathematics.get)
print(topper)
# Given string
last_name = topper.split()[0]
first_name = topper.split()[1]

full_name = first_name  +' ' + last_name

certificate_name = full_name.upper()
print(certificate_name)

# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


