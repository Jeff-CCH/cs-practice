"""
Write a Python program that can "make change." Your program should take two numbers as input, one that is a monetary amount charged and the other that is a monetary amount given. It should then return the number of each kind of bill and coin to give back as change for the difference between the amount given and the amount charged. The values assigned to the bills and coins can be based on the monetary system of any current or former government. Try to design your program so that it returns as few bills and coins as possible.
"""

def make_change(x,y):
    current_list = [1000, 500, 200, 100, 50, 10, 5, 1]
    change_list = [0 for k in range(8)]
    change = x - y
    i = 0
    while change > 0:
        if change >= current_list[i]:
            quotient = change / current_list[i]
            change = change % current_list[i]
            change_list[i] += quotient
        elif i < len(current_list) -2:
            i += 1
        else:
            change_list[-1] = change
            break
            

    for i in range(len(change_list)):
        if change_list[i] != 0:
            print "{0}:{1}".format(current_list[i],
                                   change_list[i])

def main():
    while True:
        x,y = input("Please input 2 integers, x&y, x>y: ")
        make_change(x,y)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
