# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def check_palindrome(string):
    no_whitespaces = string.upper()
    no_whitespaces = no_whitespaces.replace(' ', '')
    no_whitespaces_reverse = no_whitespaces[::-1]

    if (no_whitespaces == no_whitespaces_reverse):
        return True
    else:
        return False


string = ["Madam", "Nurses Run", "Internet of Things", "Saippuakauppias"]

for i in string:
    print(i, "is a palindrome?", check_palindrome(i))
