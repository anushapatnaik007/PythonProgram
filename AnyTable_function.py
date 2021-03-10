""" 
    Mention what this program does
"""

def get_number():
    num = int(input("Enter the multiplication table: "))
    return num
    """ 
        This function should fetch a number from user
        Input : None
        Return : an integer
    """
    #number = # Write code to prompt the user for a number
    # Check out your code behaviour by commenting the line below
    #number = int(number) # What happens if you dont perform this operation ?
    #return number


def print_mtable(num):
    for i in range(1,11):
        print(num, "x", i, "=", num*i)
    """ 
        This function prints the multiplication table of num
        Input : an integer
        Output : Display multiplication table of input integer
        Return : None
    """
    # Your solution code goes in here

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()
