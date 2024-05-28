"""
Write a function count_upper_lower that accepts a string and calculates the number of upper case letters and lower case letters.
Afterwards, the calculated letters are printed to the console - the function does not return a value.

Sample string : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected console output :
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower().
    "m".isupper() -> False
    "m".islower() -> True
    "M".isupper() -> True
    "M".islower() -> False
"""

def count_upper_lower(message: str):
    upper = 0
    lower = 0
    for i in message:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1

    print("No. of Upper case characters: " + str(upper))
    print("No. of Lower case characters: " + str(lower))


"""
Check 33

Write a function has_33 that accepts a list of integers as input parameter (method arguments) and return True if the list contains a 3 next to a 3 somewhere - if not return False.
Inside "__main__" block below, call your function at least 3 times with different input parameters. Save the return values in variables and print them to the console.

Hint: Lists can be passed to function the same way we did with primitive types (see examples below).

Following examples show the return values (not print!) of the function with different lists as input:

    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False

"""
def has_33(list: list) -> bool:
    first = 0
    for i in list:
        if i == 3 and first == 3:
            return True
        elif i == 3:
            first = 3
        else:
            first = 0

    return False


if __name__ == '__main__':
    count_upper_lower("Hello Mr. Rogers, how are you this fine Tuesday?")
    count_upper_lower("Simon says: Use 'print' in Python, to display information to the user or console.")
    count_upper_lower("Simon says: Use 'return' within functions to send a value back to the caller, which can then be stored in a variable or used in further calculations.")
    print(has_33([1, 3, 3]))
    print(has_33([1, 3, 1, 3]))
    print(has_33([3, 1, 3]))

