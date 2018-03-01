# write a program that keeps asking fpr integer input until the user provides one


# ask for input and store as an integer
while True:
    
    try:
        integer = int(raw_input("Enter an integer: "))
        
    except ValueError:
        print("Not an integer")
    break
                  
