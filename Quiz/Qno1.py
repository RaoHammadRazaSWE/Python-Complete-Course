# Q1:
ali = "hello wroa hith thei slier dkhfi"
print(ali.split(" ")[0])
# Q2:

# Creating a list (mutable and allows duplicates)
my_list = [1, 2, 3, 3, 4, 5]

# Displaying the original list
print("Original List:", my_list)

# Modifying the list (mutable)
my_list[2] = 10
print("Modified List:", my_list)

# Adding an element to the list
my_list.append(6)
print("List after appending 6:", my_list)

# Removing an element from the list
my_list.remove(3)
print("List after removing 3:", my_list)

# Q3: 
input = [1,2,3,4,5,6,3,2,2,3,6]
output = {1,2,3,5,6}
output=set(input)
print(output)

# Q4:
b = {'ali':"A",'number':1,'ali':"B"}
print(b['ali'])


# Q5:
str1 = "Artificial"
count = 0
for x in str1:
    if(x!= "i"):
        count=  count+1
    else:
        pass
    print(count)
# Q6    
list1 = [3,2,5,6,0,15,9]
sum = 0
sum1 = 0
    
for elem in list1:
    if(elem % 2 == 0):
        sum = sum + elem
        continue
    if (elem % 3 == 0):
        sum1 = sum1 + elem
print(sum, end=" ")
print(sum1)        
            
