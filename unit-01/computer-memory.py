"""
The CPU communicates with RAM via the what?
- Memory Bus

Why does the processor get a speed boost when the processor accesses nearby memory addresses in RAM one after the other?
- Because of the cache.

Given a number 103, convert it into Binary. Then, add the resulting digits in decimal. What is the result?
- 5

What is the time complexity of performing mathematical operations on fixed-width integers? What is the space complexity of a fixed-width integer?
- Time: Constant O(1)
- Space: Constant O(1)

If each slot in memory holds 8 bits and we want to store an array of 64-bit integers, how many memory addresses will be required to store an array of 5 integers?
- 40

In order to store strings in memory, each character in the string must be encoded so that it can be stored as binary. ASCII is one example of a character set. Each character in ASCII can be represented by 7 bits (although they are commonly stored as 8 bits). Given that, what is the maximum number of characters that could be in the ASCII set?
- 128
"""


"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

Examples:

csReverseIntegerBits(417) -> 267
417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
csReverseIntegerBits(267) -> 417
csReverseIntegerBits(0) -> 0
Notes:

The input integer will not be negative.
"""

def csReverseIntegerBits(n):
    x = bin(n).replace("0b", "")
    
    x = list(x)
    x.reverse()
    x = "".join(x)

    x = int(x, 2)
    return x


"""
Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII table.

Examples:

csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
01101100 -> 108 -> "l"
01100001 -> 97 -> "a"
01101101 -> 109 -> "m"
01100010 -> 98 -> "b"
01100100 -> 100 -> "d"
01100001 -> 97 -> "a"
csBinaryToASCII("") -> ""
Notes:

The input string will always be a valid binary string.
Characters can be in the range from "00000000" to "11111111" (inclusive).
In the case of an empty input string, your function should return an empty string.
"""
import re

def csBinaryToASCII(binary):
    res = ''
    x = re.findall('.{1,8}', binary)
    for s in x:
       y = chr(int(s,2))
       res += y
    return res


"""
Given a number, write a function that converts that number into a string that contains "raindrop sounds" corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operator.

Here are the rules for csRaindrop. If the input number:

has 3 as a factor, add "Pling" to the result.
has 5 as a factor, add "Plang" to the result.
has 7 as a factor, add "Plong" to the result.
does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.
Examples:

csRaindrops(28) -> "Plong"
28 has 7 as a factor, but not 3 or 5.
csRaindrops(30) -> "PlingPlang"
30 has both 3 and 5 as factors, but not 7.
csRaindrops(34) -> "34"
34 is not factored by 3, 5, or 7.
"""

def csRaindrops(number):
    raindrops = ""
    
    if number % 3 == 0:
        raindrops += "Pling"
        
    if number % 5 == 0:
        raindrops += "Plang"
        
    if number % 7 == 0:
        raindrops += "Plong"
    
    if raindrops == "":
        return str(number)

    return raindrops