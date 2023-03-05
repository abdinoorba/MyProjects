def check_pal1(str):
    

    #str = input(" Enter a String: ")

    reverse = str[::-1]

    if reverse == str:
        print("The string is palindrome")
    else:
        print("Not palindrome")

        

def check_pal2(str):

    concat = ""
    for i in range(len(str)-1, -1,-1):
        concat += str[i]
    if str == concat:
        print("The string is a palindrome")
    else:
        print("The string is Not a palindrome")


str= "madam"

check_pal1(str)
check_pal2(str)
