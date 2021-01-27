"""
What are the two primary weaknesses of a static array as a data structure?
- Fixed size
- O(n) insertions and deletions

What is the time and space complexity of slicing an array in Python?
- Time: O(n)
- Space: O(n)

Why are out-of-place algorithms generally considered to be safer?
- Because they avoid side effects
"""

"""
You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling the stock.

Example

For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.
"""

def buyAndSellStock(prices):
    if not prices:
        return 0
        
    max_prof = 0
    min_price = prices[0]
    
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_prof = max(max_prof, prices[i] - min_price)
    return max_prof


"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".
"""
from string import ascii_letters

def alphabeticShift(inputString):
    new_word = ""
    for char in inputString:
        if char in ascii_letters:
            new_word = new_word + ascii_letters[(ascii_letters.index(char) + 1) % len(ascii_letters)]
        else:
            new_word += char
    return new_word.lower()     


"""
You are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.
"""
def validParenthesesSequence(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        
        if char in mapping:
            
            if stack:
                top_elem = stack.pop()
            else:
                top_elem = "#"
                
            if mapping[char] != top_elem:
                return False
        else:
            stack.append(char)
        
    return not stack

