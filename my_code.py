

def factorial_calc(x):   #you may choose the name of the parameter
    y=1
    total =1
    if y==0:
        return 1
    else:
        while y<x+1:
            total=total*y
            y=y+1
        return total    # be sure to return the factorial


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print(factorial_calc(5))

    #After you are satisfied with your results, use input() to prompt the user for a value:
    #num = int(input("Enter value to factorialize: "))
    #print(factorial_calc(int(num)))
