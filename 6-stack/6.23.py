"""
Suppose you have three nonempty stacks R,S,and T. Describe a sequence of operations that results in S storing all elements originally in T below all of S's original elements, with both sets of those elements in their original order. The final configuration for R should be the same as its original configuration. For example, if R = [1, 2, 3], S = [4, 5], and T = [6, 7, 8, 9], the final configuration should have R = [1, 2, 3] and S = [6, 7, 8, 9, 4, 5].
"""

R = [1,2,3]
S = [4,5]
T = [6,7,8,9]

for i in range(2):
    R.push(S.pop())

for i in range(4):
    R.push(T.pop())

for i in range(6):
    S.push(R.pop())
