from sys import argv

"""
Advent of Code Day 18 Part 1
You are given a series of expressions involving addition (+), multiplication
(*), and matching open-close pairs of paranthesis(()). Any expression contained
inside paranthesis must be evaluated before its value can be used in a
containing expression. Addition and multiplication are evaluated left-to-right
with equal precedence.
Evaluate each expression and find the sum of all of their values
Part 2
Addition now takes precedence over multiplication.
Evaluate each expression and find the sum of all of their values
"""

"""
Evaluate an expression according to the rules of part 1
Assumes the expression is well-formed
"""
def eval_expr(symbols):
    #this can be solved by a stack machine with eager evaluation
    stack = []
    for i in symbols:
        if i.isnumeric():
            #if the number is the start of an expression don't operate,
            #otherwise it's guaranteed to be preceded by an operator which
            #in turn is preceded by a number, to be evaluated immediately
            #per left-to-right rules. 
            number = int(i)
            while len(stack) != 0 and stack[-1] != '(':
                operator = stack.pop()
                other_number = stack.pop()
                if operator == '+':
                    number = other_number + number
                if operator == '*':
                    number = other_number * number
            stack.append(number)
        #if an end-paranthesis is encountered, remove its corresponding
        #beginning paranthesis, guaranteed to precede the number (and it is
        #a number) at the top of the stack. From there keep applying the
        #preceding operator to the number on top of the stack and the
        #number preceding it until the containing expression is evaluated
        if i == ')':
            number = stack.pop()
            while stack[-1] != '(':
                operator = stack.pop()
                other_number = int(stack.pop())
                if operator == '+':
                    number = other_number + number
                if operator == '*':
                    number = other_number * number
            stack.pop()
            #continue the process within the expression that contained
            #the just-exited paranthetical expression
            while len(stack) != 0 and stack[-1] != '(':
                operator = stack.pop()
                other_number = int(stack.pop())
                if operator == '+':
                    number = other_number + number
                if operator == '*':
                    number = other_number * number
            stack.append(number)
        #push operators and beginning paranthesis to the stack and move on
        if i == '+' or i == '*' or i == '(':
            stack.append(i)
    return stack.pop()

"""
Evaluate an expression according to the rules of part 2
Assumes the expression is well-formed
"""
def eval_expr_precedence(symbols):
    #this can be solved by a stack machine with eager evaluation
    stack = []
    for i in symbols:
        if i.isnumeric():
            #if the number is the start of an expression don't operate,
            #otherwise it's guaranteed to be preceded by an operator which
            #in turn is preceded by a number. Evaluate immediately if the
            #operator is addition, delay evaluation otherwise
            number = int(i)
            while len(stack) != 0 and stack[-1] != '(':
                operator = stack.pop()
                other_number = stack.pop()
                if operator == '+':
                    number = other_number + number
                else:
                    stack.append(other_number)
                    stack.append(operator)
                    break
            stack.append(number)
        #if an end-paranthesis is encountered, remove its corresponding
        #beginning paranthesis, guaranteed to precede the number (and it is
        #a number) at the top of the stack. From there keep applying the
        #preceding operator to the number on top of the stack and the
        #number preceding it until the containing expression is evaluated
        if i == ')':
            number = stack.pop()
            #all additions within this expression have been performed, any
            #operator remaining is a *
            while stack[-1] != '(':
                stack.pop()
                other_number = int(stack.pop())
                number = other_number * number
            stack.pop()
            #continue the process within the expression that contained
            #the just-exited paranthetical expression
            while len(stack) != 0 and stack[-1] != '(':
                operator = stack.pop()
                other_number = int(stack.pop())
                if operator == '+':
                    number = other_number + number
                else:
                    stack.append(other_number)
                    stack.append(operator)
                    break
            stack.append(number)
        #if a * operator is encountered, multiply the preceding elements of
        #the stack until a + or the beginning of the (sub-)expression is
        #reached
        if i == '*':
            number = stack.pop()
            while len(stack) != 0 and stack[-1] != '+' and stack[-1] != '(':
                operator = stack.pop()
                other_number = stack.pop()
                #operator guaranteed to be a *, no need to check
                number = other_number * number
            stack.append(number)
            stack.append(i)
        #push operators and beginning paranthesis to the stack and move on
        if i == '+' or i == '(':
            stack.append(i)
    #similarly to the paranthesis case, evaluate for the top-level expression
    number = stack.pop()
    while len(stack) != 0:
        #operator guaranteed to be a *, no need to check
        stack.pop()
        other_number = int(stack.pop())
        number = other_number * number
    return number

if __name__ == "__main__":
    #all numbers in the input expressions are single-digit, so every
    #element is a single non-whitespace character
    f = open(argv[1], 'r')
    expressions = [i.strip().replace(" ", "") for i in f]
    f.close()
    print(sum(map(eval_expr, expressions)))
    print(sum(map(eval_expr_precedence, expressions)))
