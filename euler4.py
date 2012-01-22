def palin(n):
    y = []
    x = list(str(n))
    for i in reversed(x):
        y.append(i)
    return x == y
        
def ans():
    mx = 0
    a = []
    x = y = range(101, 1000)
    for i in x:
        for z in y:
            if palin(i * z):
                a.append(i * z)
            else:
                pass
    for num in a:
        if num > mx:
            mx = num
        else:
            pass
    return mx
    
ans()
            
        

