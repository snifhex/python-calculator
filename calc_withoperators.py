import operator
expression = input('Enter expression>\n')
operators = '+,-,/,%,*,^'

operators_dict = {
    '+': operator.add, 
    '-': operator.sub, 
    '/': operator.truediv, 
    '%': operator.mod, 
    '*': operator.mul, 
    '^': operator.pow
}

for opr in operators:
    if opr in expression:
        operands = [int(elem) for elem in expression.split(opr)]
        if len(operands)>2:
            result = operands[0]
            for i in range(1, (len(operands))):
                result = operators_dict.get(opr)(result, operands[i])
        else:
            result = operators_dict.get(opr)(int(operands[0]), operands[1])
        print(result)
