 # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# I added this comment myself now


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Presh')

#understanding the __name__ == "__main__"

def add (a, b):
    return a + b

# tracking the special variable __name__ to see how it changes b/w it's
# given value and the python file/module called main
print (__name__)

# this condition checks if we are running this main.py file here , or
# we are importing it to another file and just using the fuctions inside the main.py file
if  __name__ == "__main__" :
    print(add(11, 12))


print("Just another line of testing code")

print("second line of testing code")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
