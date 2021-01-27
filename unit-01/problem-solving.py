"""
What is the most important action to take during the Plan step of UPER?
- Taking the problem description and transforming it into a complete, actionable plan to solve that problem (oftentimes using pseudocode to do so)
"""

"""
Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.
"""

def csRemoveTheVowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in input_str:
        if vowel.lower() in vowels:
            input_str = input_str.replace(vowel, "")
    return input_str

"""
Given a string of words, return the length of the shortest word(s).

Notes:

The input string will never be empty and you do not need to validate for different data types.
"""
def csShortestWord(input_str):
    for word in input_str:
        input_str = input_str.split()
        res = min(len(str) for str in input_str)
        return int(res)



"""
Given an array of integers, return the sum of all the positive integers in the array.

Examples:

csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
csSumOfPositive([-3, -2]) -> 0
Notes:

If the input_arr does not contain any positive integers, the default sum should be 0.
"""
def csSumOfPositive(input_arr):
    sum_num = sum(num for num in input_arr if num > 0)
    return sum_num


"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
"""

def csLongestPossible(str_1, str_2):
    # combine given strings into one string
    joined_str = str_1 + str_2
    
    # sort string alphabetically
    sorted_str = ''.join(sorted(joined_str))
     
    # split string into strings by letter
    letters = ""
    res = []
    current_letter = sorted_str[0]
    for letter in sorted_str:
        if letter == current_letter:
            letters += letter
        else:
            current_letter = letter
            res.append(letters)
            letters = current_letter
    
    res.append(letters)
    print(res)
    
    # return the first index of each individual string
    output = ""
    for str in res:
        values = str[0]
        output += values
    return output


"""
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
Notes:

The output can contain the digit 5.
The start number will always be less than the end number (both numbers can also be negative)
"""

def csAnythingButFive(start, end):
    # create an empty list to add numbers that do not contain 5 to 
    res = []
    
    # loop through the range (start & end given), + 1 to end because range in non inclusive
    for number in range(start, end + 1):
        number = str(number)
        
        # check if number contains 5 
        if '5' in number:
            pass
        
        # if number does not contain 5, add number to not_five list
        else:
            number = int(number)
            res.append(number)    
            
    # return length of list
    return len(res)   