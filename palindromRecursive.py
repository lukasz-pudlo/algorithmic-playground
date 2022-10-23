def isPalindrome(letters):
    if len(letters) == 0 or len(letters) == 1:
        return True
    else:
        start = letters[0]
        end = letters[-1]
        middle = letters[1:-1]
        return start == end and isPalindrome(middle)


print(isPalindrome('amanaplanacanalpanama'))
