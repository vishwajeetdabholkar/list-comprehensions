#List Comprehensions for list of squares

print("Squares using List comprehensions")
squares = [x*x for x in range(10)]

print(squares)

#List Comprehensions for nested lists for creating matrix
#Nested lists are a common way to create matrices, which are often used for mathematical purposes

m = [[i for i in range(5)] for _ in range(6)]
for i in m:
    print("\n",i)