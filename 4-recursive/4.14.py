"""
describe a recursive algorithm for solving the hanoi tower.
"""

def solve_hanoi(n, fromPeg, toPeg, withPeg):
    if n > 1:
        solve_hanoi(n-1, fromPeg, withPeg, toPeg)
        move_disk(n, toPeg)
        solve_hanoi(n-1, withPeg, toPeg, fromPeg)
    else:
        move_disk(n, toPeg)

def move_disk(n, peg):
    print "move disk {0} to {1}".format(n, peg)


def solve_hanoi2(n, fromPeg, toPeg, withPeg, Peg1, Peg2, Peg3):
    if n == 1:
        move_disk2(n, fromPeg, toPeg)
        print Peg1, Peg2, Peg3
    else:
        solve_hanoi2(n-1, fromPeg, withPeg, toPeg, Peg1, Peg2, Peg3)
        move_disk2(n, fromPeg, toPeg)
        print Peg1, Peg2, Peg3
        solve_hanoi2(n-1, withPeg, toPeg, fromPeg, Peg1, Peg2, Peg3)

def move_disk2(n, fromPeg, toPeg):
    fromPeg.remove(n)
    toPeg.append(n)

def main():
    print "solve hanoi tower with height 4"
    solve_hanoi(4, "A", "B", "C")

    towerA = [4,3,2,1]
    towerB = []
    towerC = []
    solve_hanoi2(4, towerA, towerB, towerC, towerA, towerB, towerC)

if __name__ == '__main__':
    main()
