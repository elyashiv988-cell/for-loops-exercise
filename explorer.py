# part 1
# 1 
'''
fruits= ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

#2
print(list(range(1,6)))
#3
print(list(range(0,10,2)))

#4
for frout in enumerate(fruits):
    print(frout)
#5'
scores = {'Alpha': 80, 'Bravo': 95}
for score in scores.items():
    print(score)

# 6
sum=0
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    sum=num+sum
print(sum)
# 7

i=0
while i <5:
    i+=1
    print(i)
for i in range(1,6):
    print(i) 
# 8
matrix = [[1, 2, 3], [4, 5, 6]]
for i in matrix:
    for _ in i:
        print(_)
# 9 
squera_list=[]
for i in range(1,11):
    i=i*i
    squera_list.append(i)
print (squera_list)
# 10
for i in range(11):
    if i%2==0:
        print(i)

# part 2

# 1
names = ['Alpha', 'Bravo'] 
scores = [80, 95]
a=zip(names,scores)
print(list(a))

# 2
result=[]
for n in range(1,6):
    result.append((n,n**2))
print(result)

# 3
fruits= ['apple', 'banana', 'cherry','lemon']
for i, fruits in enumerate(fruits,start=1):
    print(i,fruits)

# 4
matrix = [[1, 2], [3, 4], [5, 6]] 
single_list=[]
for i in matrix:
    for n in i:
        single_list.append(n)
print(single_list)

# 5
words = ['hello', 'world', 'python']
uppercase=[]
for i in words:
    uppercase.append(i.upper())
print(uppercase)
'''
# part 3
# self learn
# 1 looping by value the loop runs every value in the list, and looping by index the loop runs only in the index. 
# 2 when we want to create a new list from the list By filtering the values. 
