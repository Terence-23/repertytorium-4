def rpn(s):
    s = s.strip()
    operands = []
    for i in s.split(" "):
        if 0 <= ord(i[0]) - ord('0') <= 9:
            operands.append(int(i))
        else:
            r = operands.pop()
            l = operands.pop()
            match i:
                case '-':
                    operands.append(l-r)
                case '+':
                    operands.append(l+r)
                case '*':
                    operands.append(l*r)
                case '/':
                    operands.append(l//r)
                case _:
                    return
    return operands[0]


print(rpn(input()))