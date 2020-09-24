

def factorial_calc(x):   #you may choose the name of the parameter
    x=1
    total =1
    if x==0:
        return 1
    else:
        while x<num+1:
            total=total*x
            x=x+1
        return total    # be sure to return the factorial


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
     #print(factorial_calc(1))

    #After you are satisfied with your results, use input() to prompt the user for a value:
    num = int(input("Enter value to factorialize: "))
    print(factorial_calc(int(num)))
