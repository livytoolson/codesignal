"""
If a queue only allows operations at the ends (front and back), what other data structure would work perfectly to use to build the queue?
- Linked List

In your own words, explain the strengths of a stack data structure.
- A stack can be implemented with either a linked list or a dynamic array. All operations performed with a stack are O(1). The data structure is simple but can be used to perform powerful operations.
"""

"""
Implement a queue using two stacks.

You are given an array of requests, where requests[i] can be "push <x>" or "pop". Return an array composed of the results of each "pop" operation that is performed.

Example

For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
queueOnStacks(requests) = [1, 2].

After the first request, the queue is {1}; after the second it is {1, 2}. Then we do the third request, "pop", and add the first element of the queue 1 to the answer array. The queue becomes {2}. After the fourth request, the queue is {2, 3}. Then we perform "pop" again and add 2 to the answer array, and the queue becomes {3}.
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        while right.isEmpty() != True:
            left.push(right.pop())
        left.push(x)

    def remove():
        while left.isEmpty() != True:
            right.push(left.pop())
        return right.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans


"""
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
"""

def validBracketSequence(sequence):
    open_list = ["[","{","("] 
    close_list = ["]","}",")"] 
    stack = []
     
    for i in sequence: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
    else: 
        return False

