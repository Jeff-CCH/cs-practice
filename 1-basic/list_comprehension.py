"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
"""

def main():
    print [k*(k-1) for k in range(1,11)]
    
if __name__ == '__main__':
    main()