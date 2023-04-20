
#1 Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [1, 2, 3, 4, 5]
target = 7
result = find_pairs(arr, target)
print(result)

#2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse_array(arr):
    for i in range(len(arr) // 2):
        arr[i], arr[-i - 1] = arr[-i - 1], arr[i]

arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)


#3. Write a program to check if two strings are a rotation of each other?

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    double_str2 = str2 + str2
    return str1 in double_str2

str1 = "hello"
str2 = "llohe"
if is_rotation(str1, str2):
    print("Yes, {} is a rotation of {}".format(str2, str1))
else:
    print("No, {} is not a rotation of {}".format(str2, str1))

#4. Write a program to print the first non-repeated character from a string?
def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))


#5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
n = int(input("Enter the number of disks: "))
TowerOfHanoi(n, 'A', 'C', 'B')




#6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def postfix_to_prefix(postfix):
  stack = []
  operators = set(['+', '-', '*', '/', '^'])

  for char in postfix:
    if char not in operators:
      stack.append(char)
    else:
      operand1 = stack.pop()
      operand2 = stack.pop()
      stack.append(char + operand2 + operand1)
  return stack.pop()

postfix_expression = "23+7*"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)


#8. Write a program to check if all the brackets are closed in a given code snippet.
def check_brackets(code):
    stack = []
    for char in code:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack:
                return False
            if (char == ')' and stack[-1] == '(') or \
               (char == '}' and stack[-1] == '{') or \
               (char == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False

#9. Write a program to reverse a stack.
def reverse_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)

#10. Write a program to find the smallest number using a stack.
class Stack:
    def __init__(self):
        self.items = []
        self.min_stack = []

    def push(self, item):
        self.items.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        item = self.items.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


