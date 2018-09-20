from math import *



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
    print("We will use the equation: ((y2-y1)/2),((x2-x1)/2)")
    x1 = int(input("What is x1?  "))
    y1 = int(input("What is y1?  "))
    x2 = int(input("What is x2?  "))
    y2 = int(input("What is y2?  "))
    print("The midpoint of points ({},{}) and ({},{}) is {}.".format(x1,y1,x2,y2,calc_mid_pt(x1,y1,x2,y2)))
    
    
    
    
    
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
        
    '''
    pe = ((err - lit) / lit) * 100
    return pe


    

    

def main():
    while True:
        p = input("Welcome to Math Helper! Which of the following would you like to find?(Use numbers to select):\n1)Mid Point\n2)Slope\n3)Percent Error\n>")
        if p == '1':
            mid_pt()
        if p == '2':
            slope()
        if p == '3':
            perc_err()
            
        a = input("Would you like to (1) calculate this equation again, (2) use a different formula, or (3) end this program?\n>")
        if a == '1':
            print("\n")
            
        if a == '2':
            print("\n")
            
        if a == '3':
            print("\nThanks for stopping by!")
            break
if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    