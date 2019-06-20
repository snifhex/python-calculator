import math
expression = input('Enter your expression>\n')
operators = '+,-,/,%,*,^,l'
operators_dict = {
    'add':'+', 
    'sub':'-', 
    'div':'/', 
    'modulo':'%', 
    'multi':'*', 
    'power': '^',
    'log': 'l'
}

def add(operands):
    result = sum([int(operand) for operand in operands])
    return result

def sub(operands):
    result = operands[0]
    for element in range(1, len(operands)):
        result = result-operands[element]
    return result

def div(operands):
    result = operands[0]
    for element in range(1, len(operands)):
        result = result/operands[element]
    return result

def modulo(operands):
    result = operands[0]
    for element in range(1, len(operands)):
        result = result % operands[element]
    return result

def multiply(operands):
    result = 1
    for element in operands:
        result = result * element 
    return result

def power(operands):
    result = 1
    if len(operands) <3:
        result = operands[0]**operands[1]
    else:
        print('Power function only need 2 operands, passed more than 2')
    return result

def log(operands):
    result = math.log(operands)
    return result


def calCore(operator, operands):
    if operator == operators_dict['add']:
        result = add(operands)
        return result
    elif operator == operators_dict['sub']:
        result = sub(operands)
        return result
    elif operator == operators_dict['div']:
        result = div(operands)
        return result
    elif operator == operators_dict['modulo']:
        result = modulo(operands)
        return result
    elif operator == operators_dict['multi']:
        result = multiply(operands)
        return result
    elif operator == operators_dict['power']:
        result = power(operands)
        return result
    elif operator == operators_dict['log']:
        result = log(operands)
        return result

def main():
    for operator in operators:
        if operator in expression:          
            operands = expression.split(operator) 
            if operands[0] == '':
                operands = int(operands[1])
            else:
                operands = [int(operand) for operand in operands]           
            answer = calCore(operator, operands)
            print('Your result is {}'.format(answer))

main()