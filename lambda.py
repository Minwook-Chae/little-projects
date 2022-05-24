my_lambda = lambda x: x 

# how does this work? 
odd_even = lambda x: x % 2 and 'odd' or 'even' 

# how does this work? 
def myfunc(n): 
    return lambda a : a * n 


def main(): 
    print(my_lambda(15)) 
    print(odd_even(2)) 
    print(odd_even(3)) 
    # how does this work? 
    mydoubler = myfunc(2) 
    print(mydoubler(11)) 



if __name__ == '__main__': 
    main() 
