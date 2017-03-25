# iterative implementation of nth fibionachi numbers
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


# print first 10 fibionachi numbers
for i in range(1,10):
	print fib(i);
