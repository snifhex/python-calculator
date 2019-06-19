expression = input("Enter >\n")
operataors_string = '+,-,/,'
operators = {'add':'+', 'subtract':'-','divsion' : '/', 'moduls' : '%'}

#Main calculate function
def calculate(operator, operand):
    if operator == operators['add']:
        result = operand[0]+operand[1]
        return(result)
    elif operator == operators['subtract']:
        result = operand[0]-operand[1]
        return(result)
    elif operator == operators['divsion']:
        result = operand[0]/operand[1]
        return(result)
    elif operator == operators['moduls']:
        result = operand[0]%operand[1]
        return(result)
    else:
        return('choose different operator')

for operator in operataors_string:
    if operator in expression:
        operand = expression.split(operator)
        operand = [int(elem) for elem in operand]
        result = calculate(operator, operand)
        print(result)


