if __name__ == '__main__':
    s = input()
    # This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    if any(c.isalnum() for c in s):
        print(True)
    else:
        print(False)

    # This method checks if all the characters of a string are alphabetical (a-z and A-Z).
    if any(c.isalpha() for c in s):
        print(True)
    else:
        print(False)
    
    # This method checks if all the characters of a string are digits (0-9).
    if any(c.isdigit() for c in s):
        print(True)
    else:
        print(False)
    
    # This method checks if all the characters of a string are lowercase characters (a-z).
    if any(c.islower() for c in s):
        print(True)
    else:
        print(False)
    
    # This method checks if all the characters of a string are uppercase characters (A-Z).
    if any(c.isupper() for c in s):
        print(True)
    else:
        print(False)

        
