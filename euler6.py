
def ans():
    b = 0
    y = 0
    nums = range(101)
    squares = map(lambda x: x**2, range(101))
    while len(squares) > 0:
        x = squares.pop()
        y += x
    while len(nums) > 0:
        r = nums.pop()
        b += r
    s = b ** 2
    print "The square of the sum: %d\nThe sum of the squares: %d\nAnd the difference: %d" % (y, s , s - y)    
