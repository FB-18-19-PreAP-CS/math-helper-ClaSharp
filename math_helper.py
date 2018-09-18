from math import *


def calc_slope(x1,y1,x2,y2):
    """ return slope of the line through a given set of coordinates

        >>> calc_slope(9,8,7,6)
        1.0
        
        >>> calc_slope(2,3,7,4)
        0.2
        
        >>> calc_slope(12,11,20,21)
        1.25
    """
    y3 = y2-y1
    x3 = x2-x1
    return y3/x3

def calc_mid_pt(x1,y1,x2,y2):
    """returns mid point of the line through a given set of coordinates

        >>> calc_mid_pt(6,8,5,6)
        '(5.5,7.0)'
        
        >>> calc_mid_pt(8,7,2,4)
        '(5.0,5.5)'
        
        >>> calc_mid_pt(13,28,15,20)
        '(14.0,24.0)'
    """
    y3 = (y1 + y2)/2
    x3 = (x1 + x2)/2
    return "({},{})".format(x3,y3)
    
def mid_pt():
    x1 = int(input("What is x1?  "))
    y1 = int(input("What is y1?  "))
    x2 = int(input("What is x2?  "))
    y2 = int(input("What is y2?  "))
    print("The midpoint of points ({},{}) and ({},{}) is {}.".format(x1,y1,x2,y2,calc_mid_pt(x1,y1,x2,y2)))

def slope():
    print("We will use the equation: (y2-y1)/(x2-x1)")
    x1 = int(input("What is x1?  "))
    y1 = int(input("What is y1?  "))
    x2 = int(input("What is x2?  "))
    y2 = int(input("What is y2?  "))
    print("The slope of points ({},{}) and ({},{}) is {}.".format(x1,y1,x2,y2,calc_slope(x1,y1,x2,y2)))
    

def main():
    #slope()
    mid_pt()

if __name__ == "__main__":
    #main()
    import doctest
    doctest.testmod()
    