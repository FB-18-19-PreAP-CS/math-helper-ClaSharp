from math import *


def calc_slope(x1,y1,x2,y2):
    """ return slope of the line through a given set of coordinates

        >>> calc_slope(9,8,7,6)
        1.0
        
        >>> calc_slope(2,3,7,4)
        0.2
        
        >>> calc_slope(12,11,20,21)
        
    """
    y3 = y2-y1
    x3 = x2-x1
    return y3/x3
    

def slope():
    print("We will use the equation: (y2-y1)/(x2-x1)")
    x1 = int(input("What is x1?  "))
    y1 = int(input("What is y1?  "))
    x2 = int(input("What is x2?  "))
    y2 = int(input("What is y2?  "))
    print("The slope of points ({},{}) and ({},{}) is {}.".format(x1,y1,x2,y2,calc_slope(x1,y1,x2,y2)))
    

def main():
    slope()

if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    