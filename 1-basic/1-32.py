"""
Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output device. That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be done on a separate line. After each such input, you should output to the Python console what would be displayed on your calculator.
"""

def main():
    math_expression = ''
    while True:
        string = str(input("Please input a number or a operator: "))
        if string == '=':
            print eval(math_expression)
            con = input("Continue? [y/n]: ")
            if con != 'y':
                break
        else:
            math_expression += string
      

if __name__ == '__main__':
    main()
