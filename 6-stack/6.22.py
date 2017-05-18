"""
describe a nonrecursive way of evaluating an expression in postifx notation
"""

def eval_postfix_notation(expression):
    for v in expression:
        if v not in "+-*/":
            stack.push(v)
        else:
            a = stack.pop()
            b = stack.pop()
            if v == "+": stack.push(a+b)
            elif v == "-": stack.push(a-b)
            elif v == "*": stack.push(a*b)
            else: stack.push(a/b)
