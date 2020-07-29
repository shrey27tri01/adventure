# import sys

# CURSOR_UP_ONE = '\x1b[1A'
# ERASE_LINE = '\x1b[2K'

# def delete_last_lines(n=1):
#     for _ in range(n):
#         sys.stdout.write(CURSOR_UP_ONE)
#         sys.stdout.write(ERASE_LINE)

# print("Hello")
# delete_last_lines()

# import sys
# import time

# def delete_last_line():
#     "Use this function to delete the last line in the STDOUT"

#     #cursor up one line
#     sys.stdout.write('\x1b[1A')

#     #delete last line
#     sys.stdout.write('\x1b[2K')


# ########## FOR DEMO ################
# if __name__ == "__main__":
#     print("hello")
#     print("this line will be delete after 2 seconds")
#     time.sleep(2)
#     delete_last_line()








# import time
# from datetime import datetime

# def clock():
#     while True:
#         print(datetime.now().strftime("%H:%M:%S"), end="\r")
#         time.sleep(1)

# clock()

import time
from random import randint

def rand():
    print("Ready, Set, Go.....!")
    time.sleep(1)
    numbers = []
    print("\n  ") 
    for i in range(0, 4):
        roll = randint(0, 9)
        if roll not in numbers:
            numbers.append(roll)
            print("   " + str(roll), end="\r")
            time.sleep(1)
        elif roll in numbers:
            continue;
    print(numbers)

rand()
