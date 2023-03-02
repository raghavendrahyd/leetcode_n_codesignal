# Given an encoded string, return its corresponding decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
#  Note: k is guaranteed to be a positive integer.

# For s = "4[ab]", the output should be
# decodeString(s) = "abababab";


def solution(s):
    if len(s) == 1 and s.isdigit():
        return ""
    stack = []
    for c in s:
        if c == "]":
            tmp = ""  # create a temporary string
            while stack[-1] != "[":
                tmp = stack.pop() + tmp
            stack.pop()  # pop the '['
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(tmp * int(num))  # append the string to the stack
        else:
            stack.append(c)  # append the character to the stack
    return "".join(stack)
