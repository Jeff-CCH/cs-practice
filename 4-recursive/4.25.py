"""
Provide a nonrecursive implementation of the draw interval function for the English ruler project of Section 4.1.2. There should be precisely 2^c - 1 lines of output if c represents the length of the center tick. If incrementing a counter from 0 to 2^c - 2, the number of dashes for each tick line should be exactly one more than the number of consecutive 1's at the end of the binary representation of the counter.
"""

def draw_interval(center_length):
    # gen order of interval lines
    order = '1'
    for i in range(2, center_length+1):
       order = order + str(i) + order[:len(order)] 

    for n in order:
        draw_line(int(n))

def draw_line(tick_len, tick_label=''):
    line = '-' * tick_len
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_ruler(num_inches, major_length):
    print "Draw a {0} inches with len {1} ruler".format(num_inches, major_length)
    draw_line(major_length, '0')
    for j in range(1, 1+num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
    print '\n'

def main():
    draw_ruler(2, 4)
    draw_ruler(3, 3)

if __name__ == '__main__':
    main()
