from math import *



def calc_mid_pt(x1,y1,x2,y2):
    """returns mid point of the line through a given set of coordinates

        >>> calc_mid_pt(6,8,5,6)
        '(5.5,7.0)'
        
        >>> calc_mid_pt(8,7,2,4)
        '(5.0,5.5)'
        
        >>> calc_mid_pt(13,28,15,20)
        '(14.0,24.0)'
        
        >>> calc_mid_pt(5,4,8,2)
        '(6.5,3.0)'
        
        >>> calc_mid_pt(17,31,8,40)
        '(12.5,35.5)'
    """
    y3 = (y1 + y2)/2
    x3 = (x1 + x2)/2
    return "({},{})".format(x3,y3)
    
def mid_pt():
    print("We will use the equation: ((y2-y1)/2),((x2-x1)/2)")
    x1 = int(input("What is x1?  "))
    y1 = int(input("What is y1?  "))
    x2 = int(input("What is x2?  "))
    y2 = int(input("What is y2?  "))
    if x1 == x2 and y1 == y2:
        print('There is no midpoint.')
    if x1 != x2 and y1 != y2:
        print("The midpoint of points ({},{}) and ({},{}) is {}.".format(x1,y1,x2,y2,calc_mid_pt(x1,y1,x2,y2)))
    
    
    
    
    
def calc_slope(x1,y1,x2,y2):
    """ return slope of the line through a given set of coordinates

        >>> calc_slope(9,8,7,6)
        1.0
        
        >>> calc_slope(2,3,7,4)
        0.2
        
        >>> calc_slope(12,11,20,21)
        1.25
        
        >>> calc_slope(18,11,4,4)
        0.5
        
        >>> calc_slope(27,12,2,2)
        0.4
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
    


    
    
    
def perc_err():
    print("We will use this formula: %err = ((your data - literary) / literary) * 100")
    err = int(input("What is your data?  "))
    lit = int(input("What is the official data result?  "))
    print("The percent error between your data, {}, and the official data, {}, is {}%.".format(err,lit,calc_perc_err(err,lit)))
    
    
def calc_perc_err(err,lit):
    '''returns the percent error of the problem by taking in the person's data and the official data results
        
        >>> calc_perc_err(7,8)
        -12.5
        
        >>> calc_perc_err(15,14)
        7.142857142857142
        
        >>> calc_perc_err(18,9)
        100.0
        
        >>> calc_perc_err(17,20)
        -15.0
        
        >>> calc_perc_err(6,4)
        50.0
    '''
    pe = abs(((err - lit) / lit) * 100)
    return pe




def pythag():
    print("We will use this equation: a**2 + b**2 = c**2")
    a = int(input("What is a?  "))
    b = int(input("What is b?  "))
    print("The missing length is {}.".format(a,b,calc_pythag(a,b)))
    
def calc_pythag(a,b):
    '''this finds the missing side length using "a" and "b"
        
        >>> calc_pythag(5,8)
        
        
        >>> calc_pythag(9,6)
        
        
        >>> calc_pythag(23,14)
        
        
        >>> calc_pythag(3,7)
        
        
        >>> calc_pythag(28,19)
        
    '''
    a2 = a**2
    b2 = b**2
    return (a2 + b2)//2
    

    

def main():
    while True:
        p = input("Welcome to Math Helper! Which of the following would you like to find?(Use numbers to select):\n1)Mid Point\n2)Slope\n3)Percent Error\n4)Pythagoean Theorem\n>")
        if p == '1':
            mid_pt()
        if p == '2':
            slope()
        if p == '3':
            perc_err()
        if p == '4':
            pythag()
            
        a = input("\nWould you like to:\n1) use a different formula\n2) end this program\n>")
        if a == '1':
            print("\n")
            
        if a == '2':
            print("\nThanks for stopping by!")
            break
if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    