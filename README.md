# list-comprehensions
Lists are one of the widely used data strcutures in Python programming and deveoplment.
List comprehensions provide a concise way to create lists. 
Common applications are to make new lists where each element is the result of some operations 
applied to each member of another sequence or iterable, 
or to create a subsequence of those elements that satisfy a certain condition.

For example if you want to create a list of squares then you can do it as:
```
squares = []
for x in range(10):
	squares.append(x**2)
print(squares)
```
Output:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


Using List comprehensions we can do it in one line as:
```
squares = [x**2 for x in range(10)]
print(squares)
```
Output:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
