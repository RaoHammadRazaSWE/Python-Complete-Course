# num = [1,2,3,4,5]
# result = sum(x*x for x in num if x%2==0)
# print(result)
# x = 5
# y = 2
# result = x ** y /2+1
# print(result)

keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Create a set from the keys list
set1 = set(keys)

# Convert values into a list of tuples containing corresponding pairs with keys
# Then convert these pairs into a dictionary
result_dict = dict(zip(set1, values))

print(result_dict)

keys = ['a', 'b', 'c']
values = [1,2,3]

set1 = set(keys)

result_dict = dict(zip(set1, values))
print(result_dict)
