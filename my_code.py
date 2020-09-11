# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none
##i messed up the if name == main part
##also need to add something for 0!

def factorial_calc(x):   #you may choose the name of the parameter
    pickanumber=int(input("pick a number:  "))
    x=1
    total =1
    while x<pickanumber+1:
        total=total*x
        x=x+1
    return total    # be sure to return the factorial


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
     print(factorial_calc)

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    #print(factorial_calc(int(num)))
