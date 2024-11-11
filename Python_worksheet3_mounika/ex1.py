"""1.You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
Create a variable named capitalized_fruits and use list comprehension
syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...].
"""

fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits=[fruit.title()  for fruit in fruits]
print(f'Capitalizing first character in each fruit {capitalized_fruits}')


"""2.You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
Make a variable named fruits_with_only_two_vowels. Use list comprehension to produce ['mango', 'kiwi', 'strawberry'],
a list of fruits with only two vowels."""

fruits_with_only_two_vowels=[fruit for fruit in fruits if
                             fruit.count('a')+
                             fruit.count('e')+
                             fruit.count('i')+
                             fruit.count('o')+
                             fruit.count('u')==2]
print(f'list of fruits with only two vowels {fruits_with_only_two_vowels}')

"""Given org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"], org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"],
find all similar pairs of genome sequences (one sequence from org1, one from org2) using list comprehension.
“Similar” means: similarity(seq1, seq2) > threshold"""

#calculate seq similarity
def similarity(seq1,seq2):
    match_sum= sum(1 for i,j in zip(seq1,seq2) if i==j)
    matches= match_sum/len(seq1)
    return matches

org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"]
org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"]
threshold=0.55

#generate all possible pairs
seq_pairs=[(seq1,seq2) for seq1 in org1 for seq2 in org2]
#filter similar pairs
similar_pairs= [(seq1,seq2) for seq1,seq2 in seq_pairs if similarity(seq1,seq2) > threshold]
pair=[pair for pair in similar_pairs]
print('Similar pairs are:',pair)


"""4.Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Create a dictionary of numbers and their squares,
excluding odd numbers using dictionary comprehension
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict={i:i**2  for i in numbers if i%2!=0}
print(dict)

"""5,sentence = "Hello, how are you?". Write a dictionary comprehension to map words to their reverse in a sentence.
The output should be - {'Hello,': ',olleH', 'how': 'woh', 'are': 'era', 'you?': '?uoy'}
"""

sentence="Happy Diwali.May your life shine like the Diwali lamps. May this festival of Diwali bring new happiness in your life."
sentence=sentence.split()
output={i: i[::-1] for i in sentence }
print(output)


"""6,Write  a lambda function to sort a list of strings by the last character"""
fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
reverse_str= lambda x:x[::-1]
sort_by_last_chr=sorted([reverse_str(x) for x in fruits])
sort_string=[ i[::-1] for i in sort_by_last_chr]
print(f'sorted list by last character {sort_string}')

#another way by assigning lambda function as key to the string
sort_str=sorted( fruits ,key=lambda x: x[-1])
print(f'sorted list by last character {sort_str}')

"""7.Write a Python program to rearrange positive and negative numbers in a given array using Lambda."""
from random import randint
rand_list=[randint(-10,10) for i in range(10)]
print('original list:',rand_list)
rearrange=lambda x:[i for i in x if i>=0]+[i for i in x if i<0]
result=rearrange(rand_list)
print('rearranged list:',result)

"""8.Create a logging decorator to record function calls, arguments, and return values.
For example, if we have an add function shown below and invoke it as add(2,3), create a decorator that prints the following:
	   # the decorator should print
	   Calling add with args: (2, 3), kwargs: {}
   add returned: 5

	    # add function
	    def add(a, b):
        		return a + b"""


def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f'calling {func.__name__} with args:{args},kwargs:{kwargs}')
        result=func(*args,**kwargs)
        print(f'{func.__name__} returned {result}')
    return wrapper

@log_decorator
def multiplication (a,b):
    return a*b

multiplication(2,3)


"""9,Create a decorator to measure the execution time of a function.
Please demonstrate using a sample function (add sleep for checking) and
a decorator for this sample function that measures the execution time.
"""
import time
def execute_time(func):
    def wrapper(*args):
        start_time={time.time()}
        result=func(*args)
        end_time={time.time()}
        execution_time=end_time-start_time
        print(f'Function {func.__name__} executed in {execution_time}')
        return result
    return wrapper

@execute_time
def sample_function(a,b):
    time.sleep(3)
    return a+b

sample_function(4,5)

"""10,Write a function division() that accepts two arguments. The function should be able
to catch an exception such as ZeroDivisionError, ValueError, or any unknown error you might
come across when you are doing a division operation. Also, add a “finally” construct.
"""

def division(n1,n2):
    try:
        div=n1/n2
    except ZeroDivisionError as e:
        print(f'cannot divide by zero {e}')
    except ValueError as v:
        print(f'Invalid number found {v}')
    except Exception as err:
        print(f'unknown error {err}')
    else:
        print(f'Division successful{div}')
    finally:
        print('This is a math operation function')

def main():
    while True:
        try:
          n1=int(input('Enter a number:'))
          n2=int(input('Enter another number:'))
          division(n1, n2)
          break
        except ValueError as e:
            print(f'Invalid input:{e}')

if __name__=="__main__":
    main()

"""
You're going to write an interactive calculator! User input is assumed to be a formula
that consists of a number, an operator (at least + and -), and another number,
separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
If the second input is not '+' or '-', again raise a FormulaError
If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

"""

class FormulaError(Exception):
    """Custom exception to handle formula errors."""
    pass

def parse_input(user_input):
    """Parses and validates the user input."""
    # Split the input into components
    parts = user_input.split()

    # Check if input has exactly 3 parts
    if len(parts) != 3:
        raise FormulaError("Input does not consist of three elements.")

    # Try to convert the first and third parts to floats
    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        raise FormulaError("The first or third input is not a number.")

    # Check if the second part is a valid operator
    operator = parts[1]
    if operator not in ('+', '-'):
        raise FormulaError("The operator is not '+' or '-'.")

    return num1, operator, num2

def calculate(num1, operator, num2):
    """Performs calculation based on the operator."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2

def interactive_calculator():
    """Main function to run the interactive calculator."""
    while True:
        user_input = input("Enter a formula (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Calculator exiting.")
            break

        try:
            num1, operator, num2 = parse_input(user_input)
            result = calculate(num1, operator, num2)
            print("Result:", result)

        except FormulaError as e:
            print("Formula error:", e)

# Run the interactive calculator
interactive_calculator()

