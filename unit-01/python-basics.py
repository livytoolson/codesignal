"""
Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

Examples:

csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2
csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
csWhereIsBob(["Jimmy", "Layla", "James"]) ➞ -1
Notes:

Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").
"""

def csWhereIsBob(names):
    
    if "Bob" in names:
        return names.index("Bob")
    else:
        return -1


"""
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False
Notes:

Any string that contains spaces or is empty should return False.
"""
def csAlphanumericRestriction(input_str):
    if input_str.isdigit():
        return True
    elif input_str.isalpha():
        return True
    else:
        return False



"""
Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
Notes:

The input string will only contain alpha characters.
"""
def csOppositeReverse(txt):
    new_txt = txt[::-1]
    new_txt = new_txt.swapcase()
    return new_txt



"""
Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9
"""
def csSquareAllDigits(n):
    res = ''
    for digit in str(n):
        res = res + str((int(digit))**2)
    return int(res)



"""
Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

Examples:

csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"
Notes:

1 <= years <= 10
1 <= groups <=26
""" 
def csSchoolYearsAndGroups(years, groups):
    res = []
    for i in range(1, years + 1):
        for j in range(97, groups + 97):
            # print(i, chr(j))
            res.append(f"{i}{chr(j)}")
            
    return ", ".join(res)



"""
Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, ignore that chord.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []
Notes:

Return an empty list if the given list is empty.
You can expect all the tests to have valid chords.
"""
def csMakeItJazzy(chords):
    chord_list = []
    for chord in chords:
        if chord[-1] == "7":
            chord_list.append(chord)
        else:
            chord_list.append(f"{chord}7")
    return chord_list