'''
--- Day 6: Trash Compactor ---
After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?

Solution:
 - Parse the input into a list of problems, each with its numbers and operator.
 - For each problem, perform the specified operation on the numbers.
 - Sum the results of all problems and return the grand total.

 --- Part Two ---
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?

Solution:
 - Reparse the input into a list of problems, generating new lists of numbers for each problem by reading the columns from right to left.
 - For each problem, perform the specified operation on the numbers and sum the results, returning the grand total, as before. 
 '''

input = '''
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
'''

input = open('input-06.txt').read()

# Part One Parsing
lines = []
problems_numbers = []
problems_operators = []
for line in input.strip().split('\n'):
    elements = [element for element in line.split(' ') if element]
    lines.append(elements)
    for i, element in enumerate(elements):
        if element.isdigit():
            if len(problems_numbers) < i + 1:
                problems_numbers.append([int(element)])
            else:
                problems_numbers[i].append(int(element))
        else:
            problems_operators.append(element)

# print(lines)
# print(problems_numbers)
# print(problems_operators)

# Part One Calculation
quantity_of_problems = len(problems_numbers)

total = 0

for i in range(quantity_of_problems):
    numbers = problems_numbers[i]
    operator = problems_operators[i]
    if operator == '+':
        result = sum(numbers)
    elif operator == '*':
        result = 1
        for number in numbers:
            result *= number
    # print(f"Problem {i+1}: {' '.join(map(str, numbers))} {operator} = {result}")
    total += result

print("Part One - Total of all problems:", total)

# Part Two Parsing
number_of_positions = []
for line in input.strip().split('\n')[:-1]:
    for i, character in enumerate(line):
        if character.isdigit():
            if len(number_of_positions) < i + 1:
                number_of_positions.append(character)
            else:
                number_of_positions[i] += character
        else:
            if len(number_of_positions) < i + 1:
                number_of_positions.append('')

# print(problems_operators)
# print(number_of_positions)

# Part Two Calculation
problem = 0
total = 0
result = 1 if problems_operators[problem] == '*' else 0
for number in number_of_positions:
    if number:
        if problems_operators[problem] == '+':
            result += int(number)
        elif problems_operators[problem] == '*':
            result *= int(number)
    else:
        total += result
        problem += 1
        if problems_operators[problem] == '+':
            result = 0
        elif problems_operators[problem] == '*':
            result = 1

total += result

print("Part Two - Total of all problems:", total)
    