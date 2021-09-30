def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        counter = counter + 1 if string[i:].startswith(sub_string) else counter
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)