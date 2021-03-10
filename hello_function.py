def get_username():
    inp = input("Enter username: ")
    return inp
    
def say_hello(msg):
    print("Hello",msg)
    
def main():
    name=get_username()
    say_hello(name)


main()
