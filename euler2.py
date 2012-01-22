def fib():
    global y
    y = []
    a, b = 0, 1
    while a < 4000001:
        y.append(a)
        a, b = b, a + b
    
def adder(s):
    x = 0
    for i in s:
        if i % 2 == 0:
            x += i
        else:
            pass
    print x

fib()
adder(y)
