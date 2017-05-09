"""
Write a short recursive Python function that rearranges a sequence of integer values so that all the even values appear before all the odd values.
"""

def rearrange(data, word=''):
    if len(data) == 0:
        print word
    else:
        if int(data[0]) % 2 == 0: rearrange(data[1:], data[0] + word)
        else: rearrange(data[1:], word + data[0])

def main():
    rearrange('11221')
    rearrange('12121')
    rearrange('11122')
    rearrange('22111')

if __name__ == '__main__':
    main()
