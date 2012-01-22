def euler1():
    y = 0
    for i in range(1000):
        if i % 3 == 0:
            y += i
        elif i % 5 == 0:
            y += i
        else:
            pass
    print y
