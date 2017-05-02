"""
Write a Python program that inputs a polynomial in standard algebraic notation and outputs the first derivative of that polynomial.
"""

# Input Format: x^2+6x-1
# cases like "azx^2" "5x*6x" "x**2" "6x/3" are not handled

def derivative(algebra):
    if "+" in algebra or "-" in algebra:
        if "+" in algebra:
            p_index = algebra.index("+")
        else: p_index = len(algebra)
        if "-" in algebra:
            m_index = algebra.index("-")
        else: m_index = len(algebra)
        index = min(p_index, m_index)
        return derivative(algebra[:index]) + algebra[index] + derivative(algebra[index+1:])
    else:
        if "x" not in algebra:
            return "0"
        elif "^" in algebra:
            e_index = algebra.index("^")
            e_q = algebra[e_index+1]
            if e_index != 1:
                p_q = str(int(e_q) * int(algebra[:e_index-1]))
            else: p_q = e_q
            return p_q + algebra[e_index-1] + algebra[e_index] + str(int(e_q) - 1)
        else:
            return algebra[:len(algebra)-1]

def main():
    while True:
        algebra = input("Please input an algebra notation: ")
        print derivative(algebra)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
