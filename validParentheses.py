"""
VALID PARENTHESES
-----------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s):
  if s == '':
      return True
  elif len(s) == 1:
      return False

  stack = [s[0]]
  for i in range(1, len(s)):
      if s[i] == ')':
          if stack and stack[-1] == '(':
              stack.pop()
          else:
              return False
      elif s[i] == '}':
          if stack and stack[-1] == '{':
              stack.pop()
          else:
              return False
      elif s[i] == ']':
          if stack and stack[-1] == '[':
              stack.pop()
          else:
              return False
      else:
          stack.append(s[i])

  if stack == []:
      return True
  return False
