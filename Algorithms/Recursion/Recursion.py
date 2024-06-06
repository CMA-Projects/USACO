# Python demonstration of Recursion

def printFun(input):
    if (input < 1):
        return # base case
    else:
        print(input, end = " ")
        printFun(input - 1) # recursive statement
        print(input, end = " ")
        return # base case
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def sum_list(list):
    if len(list == 0):
        return 0
    else:
        list[0] + sum_list(list[1:])

    
if __name__ == "__main__":
    print(factorial(4))

