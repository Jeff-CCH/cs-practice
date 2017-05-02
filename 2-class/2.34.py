"""
Write a Python program that inputs a document and then outputs a bar- chart plot of the frequencies of each alphabet character that appears in that document.
"""

def cnt_freq(data):
    d_list = [0] * 128
    for d in data:
        d_list[ord(d)] += 1
    return d_list

def main():
    while True:
        in_str = input("Please provide the content: ")
        result = cnt_freq(in_str)
        for i in range(len(result)):
            if result[i] != 0:
                print "{0}:{1}".format(chr(i), result[i])
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
