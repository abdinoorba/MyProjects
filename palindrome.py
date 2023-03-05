# s = input(" Enter a String: ")
#
# reverse = s[::-1]
#
# if reverse == s:
#     print("The string is palindrome")
# else:
#     print("Not palindrome")


def check_pal(str):

    concat = ""
    for i in range(len(str)-1, -1,-1):
        concat += str[i]
    if str == concat:
        print("The string is a palindrome")
    else:
        print("The string is Not a palindrome")


str= "madam"

check_pal(str)
