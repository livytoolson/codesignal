"""
Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

Examples:

csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]
Notes:

Your solution should be "in-place" with O(1) space complexity. Although many in-place functions do not return the modified input, in this case you should.
You should try using a "two-pointers approach".
Avoid using any built-in reverse methods in the language you are using (the goal of this challenge is for you to implement your own method).
"""

def csReverseString(chars):
    x = chars[::-1]
    return x


"""
A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:

csCheckPalindrome("racecar") -> true
csCheckPalindrome("anna") -> true
csCheckPalindrome("12345") -> false
csCheckPalindrome("12321") -> true
Notes:

Try to solve this challenge without using the reverse of the input string; use a for loop to iterate through the string and make the necessary comparisons.
Something like the code below might be your first intuition, but can you figure out a way to use a for loop instead?
def csCheckPalindrome(input_str):
    return input_str == "".join(reversed(input_str))
"""

def csCheckPalindrome(input_str):
    for i in range(0, len(input_str) - 1):
        if input_str[i] == input_str[i-1]:
            return True
        else:
            return False

"""
Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

Examples:

`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
"""
def csRemoveDuplicateWords(input_str):
    res = []
    input_str = input_str.split()
    [res.append(x) for x in input_str if x not in res]
    return " ".join(res)
