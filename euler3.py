def primef(x):
    factors = []
    y = [2, 3, 5, 7, 9]
    for i in y:
        if x % i == 0:
            factors.append(x/i) 
    print factors
            
         
