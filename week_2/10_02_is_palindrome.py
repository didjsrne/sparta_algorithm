input = "소주만병만주소"


def is_palindrome(string):  # is_palindrome("소주만병만주소")
    # is_palindrome("주만병만주")
    # is_palindrome("만병만")
    # is_palindrome("병") True
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])


print(is_palindrome(input))