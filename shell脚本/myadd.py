


#!/usr/bin/python3


import sys

def main():
    if len(sys.argv) != 3:
       print('Usage: mypyadd <num1> <num2>')
       return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = num1 + num2
        print('Result:', result)
    except ValueError:
        print('Invalid input. Please enter integer numbers.')

if __name__ == '__main__':

    main()
