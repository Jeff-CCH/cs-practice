"""
Write a Python program that simulates a handheld calculator. Your program should process input from the Python console representing buttons that are "pushed," and then output the contents of the screen after each operation is performed. Minimally, your calculator should be able to process the basic arithmetic operations and a reset/clear operation.
"""

def clear_list(input_list):
    del input_list[:]

def main():
    math_expression = []
    while True:
        input1 = str(input("Please input a number or a operator: "))
        if isinstance(input1, int):
            math_expression.append(str(input1))
        else:
            if input1 == 'reset':
                print 0
                clear_list(math_expression)
            else:
                if len(math_expression) == 3:
                    expression = ''.join(math_expression)
                    clear_list(math_expression)
                    math_expression.append(str(eval(expression)))
                    print math_expression[0]
                if input1 != '=':
                    math_expression.append(input1)
                else:
                    clear_list(math_expression)

if __name__ == '__main__':
    main()
