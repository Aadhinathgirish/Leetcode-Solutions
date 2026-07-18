def problem(s):
    stack = []
    for c in s:
        if c.isalpha():
            stack.append('1')
        else:
            stack.append(c)
    m = ''.join(stack)
    return eval(m)

print(problem('2a-3b-5'))
