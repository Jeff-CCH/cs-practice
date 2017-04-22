"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""

def main():
    out_list = []
    while True:
        try:
            input_d = input("Input a line until EOFError: ")
            out_list.append(input_d)
        except EOFError:
            for k in range(-1, len(out_list)*(-1)-1, -1):
                print out_list[k]
                break
    
if __name__ == '__main__':
    main()