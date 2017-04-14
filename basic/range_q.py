"""
What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
"""

print range(50, 90, 10)

"""
What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, -2, -4, -6, -8
"""

print range(8, -10, -2)

"""
Demonstrate how to use Python's list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
print [2**k for k in range(9)]
