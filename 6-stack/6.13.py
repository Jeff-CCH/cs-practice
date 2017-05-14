"""
Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8), in this order. Suppose further that you have an initially empty queue Q. Give a code fragment that uses only D and Q (and no other variables) and results in D storing the elements in the order (1,2,3,5,4,6,7,8)
"""

D = (1,2,3,4,5,6,7,8)
S = ()

D.addLast(D.popFirst()) # 2,3,4,5,6,7,8,1 | ()
D.addLast(D.popFirst()) # 3,4,5,6,7,8,1,2 | ()
D.addLast(D.popFirst()) # 4,5,6,7,8,1,2,3 | ()
D.addLast(D.popFirst()) # 5,6,7,8,1,2,3,4 | ()
S.enque(D.popFirst())    # 6,7,8,1,2,3,4 | 5
S.enque(D.popLast())    # 6,7,8,1,2,3 | 5,4
S.enque(D.popLast())    # 6,7,8,1,2 | 5,4,3
S.enque(D.popLast())    # 6,7,8,1 | 5,4,3,2
S.enque(D.popLast())    # 6,7,8 | 5,4,3,2,1
S.enque(D.popFirst())    # 7,8 | 5,4,3,2,1,6
S.enque(D.popFirst())    # 8 | 5,4,3,2,1,6,7
S.enque(D.popFirst())    # () | 5,4,3,2,1,6,7,8
D.addFirst(S.deque())    # (5) | 4,3,2,1,6,7,8
D.addLast(S.deque())    # (5,4) | 3,2,1,6,7,8
D.addFirst(S.deque())    # (3,5,4) | 2,1,6,7,8
D.addFirst(S.deque())    # (2,3,5,4) | 1,6,7,8
D.addFirst(S.deque())    # (1,2,3,5,4) | 6,7,8
D.addLast(S.deque())    # (1,2,3,5,4,6) | 7,8
D.addLast(S.deque())    # (1,2,3,5,4,6,7) | 8
D.addLast(S.deque())    # (1,2,3,5,4,6,7,8) | ()

